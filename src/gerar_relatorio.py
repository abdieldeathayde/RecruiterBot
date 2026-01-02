import whisper
import os
from statistics import mean
import shutil
import scipy.io.wavfile as wavfile
import numpy as np
import warnings

# Suprimir aviso de FP16
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")

# =============================
# CONFIGURAÇÃO DO WHISPER
# =============================
def carregar_modelo():
    """Carrega o modelo Whisper com tratamento de erro para cache corrompido"""
    try:
        model = whisper.load_model("base")
        return model
    except RuntimeError as e:
        if "checksum does not match" in str(e):
            print("⚠️ Cache do modelo corrompido. Limpando cache...")
            cache_dir = os.path.expanduser("~/.cache/whisper")
            if os.path.exists(cache_dir):
                shutil.rmtree(cache_dir)
                print("✅ Cache removido. Baixando modelo novamente...")
            model = whisper.load_model("base")
            return model
        else:
            raise

model = carregar_modelo()

# =============================
# FUNÇÕES DE AVALIAÇÃO
# =============================
def avaliar_resposta(texto):
    palavras = texto.split()
    qtd = len(palavras)

    criterios = {
        "clareza": 3,
        "objetividade": 3,
        "profundidade": 3,
        "estrutura": 3,
        "exemplos": 2,
        "maturidade": 3
    }

    if qtd > 120:
        criterios["profundidade"] += 1
    if qtd < 40:
        criterios["profundidade"] -= 1

    if qtd < 80:
        criterios["objetividade"] += 1

    if any(p in texto.lower() for p in ["exemplo", "resultado", "impacto", "aprendi", "situação"]):
        criterios["exemplos"] += 2

    if any(p in texto.lower() for p in ["primeiro", "depois", "por fim", "então"]):
        criterios["estrutura"] += 1

    if any(p in texto.lower() for p in ["acho", "talvez", "meio", "coisa"]):
        criterios["clareza"] -= 1

    for k in criterios:
        criterios[k] = max(1, min(5, criterios[k]))

    return criterios


def gerar_feedback(criterios):
    feedback = []

    if criterios["exemplos"] <= 2:
        feedback.append("Incluir exemplos concretos aumentaria a credibilidade da resposta.")

    if criterios["objetividade"] <= 2:
        feedback.append("A resposta pode ser mais direta, reduzindo rodeios.")

    if criterios["estrutura"] <= 2:
        feedback.append("Estruturar melhor a resposta (início, meio e fim) ajudaria na clareza.")

    if not feedback:
        feedback.append("Resposta bem estruturada e alinhada ao padrão profissional.")

    return feedback


# =============================
# CARREGAR ÁUDIO SEM FFMPEG
# =============================
def carregar_audio(caminho_arquivo):
    """Carrega arquivo WAV sem depender de FFmpeg"""
    try:
        sample_rate, audio_data = wavfile.read(caminho_arquivo)
        
        # Converter para mono se estéreo
        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)
        
        # Normalizar para float32 no intervalo [-1, 1]
        if audio_data.dtype != np.float32:
            if audio_data.dtype == np.int16:
                audio_data = audio_data.astype(np.float32) / 32768.0
            elif audio_data.dtype == np.int32:
                audio_data = audio_data.astype(np.float32) / 2147483648.0
            else:
                audio_data = audio_data.astype(np.float32)
        
        # Resample para 16kHz se necessário (padrão do Whisper)
        if sample_rate != 16000:
            from scipy.interpolate import interp1d
            num_samples = int(len(audio_data) * 16000 / sample_rate)
            old_indices = np.arange(len(audio_data))
            new_indices = np.linspace(0, len(audio_data) - 1, num_samples)
            f = interp1d(old_indices, audio_data, kind='linear')
            audio_data = f(new_indices)
        
        # Garantir que está em float32 (Whisper requer isso)
        audio_data = audio_data.astype(np.float32)
        
        return audio_data
    except Exception as e:
        print(f"⚠️ Erro ao carregar áudio {caminho_arquivo}: {e}")
        return None


# =============================
# RELATÓRIO FINAL (TXT)
# =============================
def gerar_relatorio_profissional():
    print("\n📊 Gerando relatório profissional...\n")

    resultados_finais = []

    with open("relatorio_profissional.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO PROFISSIONAL DE ENTREVISTA – RH\n")
        f.write("=" * 70 + "\n\n")

        for arquivo in sorted(os.listdir("audios")):
            if not arquivo.endswith(".wav"):
                continue

            caminho = os.path.join("audios", arquivo)
            
            # Carregar áudio sem FFmpeg
            audio = carregar_audio(caminho)
            if audio is None:
                print(f"❌ Pulando {arquivo}")
                continue
            
            # Transcrever usando Whisper
            transcricao = model.transcribe(audio, language="pt")["text"]

            criterios = avaliar_resposta(transcricao)
            feedback = gerar_feedback(criterios)
            media = round(mean(criterios.values()), 2)

            resultados_finais.append(media)

            f.write(f"🎙️ Arquivo: {arquivo}\n")
            f.write("-" * 70 + "\n")
            f.write("TRANSCRIÇÃO:\n")
            f.write(transcricao + "\n\n")

            f.write("AVALIAÇÃO POR COMPETÊNCIA:\n")
            for k, v in criterios.items():
                f.write(f"- {k.title()}: {v}/5\n")

            f.write(f"\nNOTA MÉDIA DA RESPOSTA: {media}/5\n\n")

            f.write("FEEDBACK DO RH:\n")
            for item in feedback:
                f.write(f"- {item}\n")

            f.write("\n" + "=" * 70 + "\n\n")

        nota_final = round(mean(resultados_finais), 2)

        f.write(f"📈 NOTA FINAL DA ENTREVISTA: {nota_final}/5\n")

        if nota_final >= 4:
            f.write("STATUS: Perfil fortemente recomendado.\n")
        elif nota_final >= 3:
            f.write("STATUS: Perfil compatível, com pontos de desenvolvimento.\n")
        else:
            f.write("STATUS: Perfil abaixo do esperado para o momento.\n")

    print("✅ Relatório gerado com sucesso: relatorio_profissional.txt")


if __name__ == "__main__":
    gerar_relatorio_profissional()
