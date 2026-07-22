import os
from datetime import datetime

from xp import adicionar_xp
from conquistas import desbloquear
from missoes import concluir_missao

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def conversar(especialidade):
    print("\n========================")
    print(especialidade)
    print("Digite voltar para retornar ao menu.")
    print("========================\n")

    historico = []

    while True:
        pergunta = input("Você: ").strip()

        if not pergunta:
            continue

        if pergunta.lower() == "voltar":
            break

        historico.append(f"Aluno: {pergunta}")

        contexto = "\n".join(historico)

        prompt = f"""
Você é um professor especialista em {especialidade}.
Explique conceitos de forma simples.
Considere que o aluno está no segundo semestre de Sistemas de Informação.

Sempre:
Explique passo a passo.
Dê exemplos.
Mostre aplicações práticas.
Se possível, mostre código Python.
Sugira exercícios.
Responda em português do Brasil.

Histórico da conversa:

{contexto}

Nova pergunta do aluno:

{pergunta}
"""

        try:
            resposta = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        except Exception as erro:
            print("\nErro ao acessar a IA:")
            print(erro)
            continue

        print("\nMentor:")
        print(resposta.text)
        
        concluir_missao("ia")
        desbloquear("Primeira conversa com IA")

        historico.append(f"Mentor: {resposta.text}")
        historico = historico[-10:]
        
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print("TESTE DATETIME")
        
        with open("historico.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"[{agora}]\n")
            arquivo.write(f"Aluno: {pergunta}\n")
            arquivo.write(f"Mentor: {resposta.text}\n")
            arquivo.write("-" * 50 + "\n")
        
        xp = adicionar_xp(5)

        print(f"\n🎉 +5 XP por estudar!")
        print(f"⭐ XP Atual: {xp}")

        print()
