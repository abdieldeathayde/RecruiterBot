import pyttsx3
import speech_recognition as sr
import soundfile as sf
import time
import os

# =============================
# CONFIGURAÇÃO DE VOZ
# =============================
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def falar(texto):
    print(f"\n🧑‍💼 RH: {texto}")
    engine.say(texto)
    engine.runAndWait()

# =============================
# OUVIR E GRAVAR ÁUDIO
# =============================
def ouvir_e_gravar(nome_arquivo):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Responda agora (até 5 minutos)...")
        r.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = r.listen(
                source,
                timeout=15,
                phrase_time_limit=300
            )
        except sr.WaitTimeoutError:
            print("⏱️ Nenhuma resposta iniciada.")
            return None

    with open(nome_arquivo, "wb") as f:
        f.write(audio.get_wav_data())

    print(f"💾 Áudio salvo em {nome_arquivo}")
    return nome_arquivo

# =============================
# ENTREVISTA
# =============================
def entrevista_rh():
    perguntas = [
        "Pode se apresentar brevemente, falando sobre sua trajetória?",
        "Por que você se interessou por esta vaga?",
        "Conte sobre um desafio profissional ou acadêmico que você enfrentou.",
        "Quais são seus principais pontos fortes?",
        "Onde você se vê profissionalmente nos próximos anos?"
    ]

    os.makedirs("audios", exist_ok=True)

    print("=" * 60)
    print("🎧 ENTREVISTA DE RH — MODO REALISTA")
    print("🕒 Até 5 minutos por resposta")
    print("=" * 60)

    for i, pergunta in enumerate(perguntas, start=1):
        time.sleep(2)
        falar(f"Pergunta {i}. {pergunta}")
        ouvir_e_gravar(f"audios/resposta_{i}.wav")

    falar("A entrevista foi encerrada. Obrigado pela sua participação.")
    print("✅ Entrevista finalizada.")

if __name__ == "__main__":
    entrevista_rh()
