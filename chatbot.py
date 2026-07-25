# Banco de dados
from database.banco import criar_banco
from autenticacao import autenticar
from services.dashboard_service import obter_dashboard

# Interface
from dashboard import mostrar_dashboard

# Estudos
from estudos import plano_estudos, ver_planos
from quiz import quiz_python
from ia import conversar

# Conquistas
from conquistas import mostrar_conquistas

# Relatórios
from historico import mostrar_historico
from desempenho import mostrar_desempenho
from relatorio import mostrar_relatorio


def main():
    
    criar_banco()

    usuario = autenticar()

    if usuario is None:
        print("\nAté a próxima!")
        return

    nome = usuario[1]
    usuario_id = usuario[0] 

    while True:

        # Atualiza informações do Dashboard
        dashboard = obter_dashboard(usuario_id)

        mostrar_dashboard(
            usuario_id,
            nome,
            dashboard["rank"],
            dashboard["nivel"],
            dashboard["xp"],
            dashboard["barra"],
            dashboard["porcentagem"],
            dashboard["limite"],
            dashboard["quizzes"],
            dashboard["total_conquistas"],
            dashboard["media"],
            dashboard["streak"],
        )

        opcao = input("\nEscolha uma opção: ").strip()
        
        if not opcao:
            continue

        if opcao == "1":
            conversar(usuario_id, "Python")

        elif opcao == "2":
            conversar(usuario_id, "Algoritmos")

        elif opcao == "3":
            conversar(usuario_id, "Banco de Dados")

        elif opcao == "4":
            conversar(usuario_id, "Redes de Computadores")

        elif opcao == "5":
            conversar(usuario_id, "Inteligência Artificial")

        elif opcao == "6":
            conversar(usuario_id, "Projetos para Portfólio e GitHub")

        elif opcao == "7":
            conversar(usuario_id, "Carreira em Tecnologia")

        elif opcao == "8":
            conversar(usuario_id, "Exercícios")

        elif opcao == "9":
            plano_estudos(usuario_id)
                 
        elif opcao == "10":
            ver_planos(usuario_id)

        elif opcao == "11":
            quiz_python(usuario_id)

        elif opcao == "12":
            mostrar_historico(usuario_id)

        elif opcao == "13":
            mostrar_conquistas(usuario_id)

        elif opcao == "14":
            mostrar_relatorio(usuario_id)

        elif opcao == "15":
            mostrar_desempenho(usuario_id)

        elif opcao == "0":
            print("\nAté a próxima!")
            break

        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()