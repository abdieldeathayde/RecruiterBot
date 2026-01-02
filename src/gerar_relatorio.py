import whisper
import os

# =============================
# CARREGAR MODELO WHISPER
# =============================
model = whisper.load_model("base")  # use "small" ou "medium" para mais precisão

# =============================
# ANÁLISE DE TEXTO
# =============================
def analisar_resposta(texto):
    palavras = texto.split()
    tamanho = len(palavras)

    score = {
        "clareza": 2,
        "objetividade": 2,
        "profundidade": 2
    }

    if tamanho > 80:
        score["profundidade"] += 1
    if tamanho < 30:
        score["objetividade"] -= 1

    if any(p in texto.lower() for p in ["exemplo", "resultado", "aprendi", "impacto"]):
        score["clareza"] += 1

    return score

# =============================
# GERAR RELATÓRIO
# =============================
def gerar_relatorio():
    print("\n📊 GERANDO RELATÓRIO DE DESEMPENHO...\n")

    relatorio = []

    for arquivo in sorted(os.listdir("audios")):
        if arquivo.endswith(".wav"):
            caminho = f"audios/{arquivo}"
            resultado = model.transcribe(caminho, language="pt")

            texto = resultado["text"]
            score = analisar_resposta(texto)

            relatorio.append((arquivo, texto, score))

    with open("relatorio_entrevista.txt", "w", encoding="utf-8") as f:
        for arquivo, texto, score in relatorio:
            f.write(f"{arquivo}\n")
            f.write(f"TRANSCRIÇÃO:\n{texto}\n")
            f.write("AVALIAÇÃO:\n")
            for k, v in score.items():
                f.write(f"- {k.title()}: {v}/5\n")
            f.write("-" * 60 + "\n")

    print("✅ Relatório gerado: relatorio_entrevista.txt")

if __name__ == "__main__":
    gerar_relatorio()
