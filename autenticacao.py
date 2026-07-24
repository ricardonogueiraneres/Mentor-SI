from login import criar_usuario, fazer_login


def autenticar():

    while True:

        print("\n==============================")
        print("        🎓 MENTOR SI")
        print("==============================")
        print("1 - Entrar")
        print("2 - Criar conta")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":

            usuario = input("Usuário: ")
            senha = input("Senha: ")

            dados = fazer_login(usuario, senha)

            if dados:
                print(f"\nBem-vindo, {dados[1]}!")
                return dados

            print("\nUsuário ou senha incorretos.")

        elif opcao == "2":

            nome = input("Nome: ")
            usuario = input("Usuário: ")
            senha = input("Senha: ")

            if criar_usuario(nome, usuario, senha):
                print("\nConta criada com sucesso!")

            else:
                print("\nEsse usuário já existe.")

        elif opcao == "0":
            return None

        else:
            print("\nOpção inválida.")