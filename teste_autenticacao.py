from login import fazer_login

usuario = fazer_login("joao", "123456")

if usuario:
    print("✅ Login realizado com sucesso!")
    print(usuario)
else:
    print("❌ Usuário ou senha inválidos.")