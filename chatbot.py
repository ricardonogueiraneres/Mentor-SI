# Banco de dados
from banco import criar_banco
from autenticacao import autenticar

# Perfil e progresso
from xp import carregar_xp, nivel_xp, barra_xp
from streak import atualizar_streak
from conquistas import (
    carregar_conquistas,
    mostrar_conquistas,
)

# Estudos
from estudos import plano_estudos, ver_planos
from quiz import quiz_python
from ia import conversar

# Relatórios
from dashboard import mostrar_dashboard
from historico import mostrar_historico
from desempenho import mostrar_desempenho
from relatorio import mostrar_relatorio

# Estatísticas
from estatisticas import (
    total_quizzes,
    media_quizzes,
    nivel_aluno,
)



def main():
    
    criar_banco()

    usuario = autenticar()

    if usuario is None:
        return

    nome = usuario[1] 

    while True:

        # Atualiza informações do Dashboard
        quizzes = total_quizzes()
        xp = carregar_xp(usuario[0])
        barra, porcentagem, limite = barra_xp(xp)
        media = media_quizzes()
        nivel = nivel_aluno(media)
        rank = nivel_xp(xp)
        streak = atualizar_streak()
        conquistas = carregar_conquistas()

        total_conquistas = len(conquistas)

        mostrar_dashboard(
            nome,
            rank,
            nivel,
            xp,
            barra,
            porcentagem,
            limite,
            quizzes,
            total_conquistas,
            media,
            streak,
        )

        opcao = input("\nEscolha uma opção: ").strip()
        
        if not opcao:
            continue

        if opcao == "1":
            conversar("Python")

        elif opcao == "2":
            conversar("Algoritmos")

        elif opcao == "3":
            conversar("Banco de Dados")

        elif opcao == "4":
            conversar("Redes de Computadores")

        elif opcao == "5":
            conversar("Inteligência Artificial")

        elif opcao == "6":
            conversar("Projetos para Portfólio e GitHub")

        elif opcao == "7":
            conversar("Carreira em Tecnologia")

        elif opcao == "8":
            conversar("Exercícios")

        elif opcao == "9":
            plano_estudos()
                 
        elif opcao == "10":
            ver_planos()

        elif opcao == "11":
            quiz_python()

        elif opcao == "12":
            mostrar_historico()

        elif opcao == "13":
            mostrar_conquistas()

        elif opcao == "14":
            mostrar_relatorio()

        elif opcao == "15":
            mostrar_desempenho()

        elif opcao == "0":
            print("\nAté a próxima!")
            break

        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main()