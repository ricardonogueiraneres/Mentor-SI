from datetime import datetime

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("TESTE DATETIME")
print(agora)

with open("historico.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"[{agora}]\n")
    arquivo.write("Aluno: TESTE DATETIME\n")
    arquivo.write("Mentor: RESPOSTA DE TESTE\n")
    arquivo.write("-" * 50 + "\n")
