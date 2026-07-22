from datetime import datetime
from recomendacoes import gerar_recomendacao

LINHA = "══════════════════════════════════════════════"

def mostrar_dashboard(
    nome: str,
    rank: str,
    nivel: int,
    xp: int,
    barra: str,
    porcentagem: int,
    limite: int,
    quizzes: int,
    total_conquistas: int,
    media: float,
    streak: int,
) -> None:
    """
    Exibe o painel principal do Mentor SI.
    """

    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║                  🎓 MENTOR SI 6.0                   ║")
    print("║             Seu Professor de TI com IA              ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║ 📅 {agora:<47} ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    print("══════════════ 👤 PERFIL ══════════════")
    print(f"👤 Aluno............... {nome}")
    print(f"🎖️ Rank................ {rank}")
    print(f"🏆 Nível............... {nivel}")
    texto = "dia" if streak == 1 else "dias"
    print(f"🔥 Sequência........... {streak} {texto}")

    print("\n══════════════ ⭐ PROGRESSO ═════════════")
    print(f"⭐ XP.................. {xp}")
    print(f"📊 Barra............... {barra} {porcentagem}%")
    print(f"🎯 Próximo nível....... {limite} XP")

    print("\n══════════════ 📊 ESTATÍSTICAS ═════════════")
    print(f"🧠 Quizzes............ {quizzes}")
    print(f"🏅 Conquistas......... {total_conquistas}")
    print(f"📈 Média.............. {media:.1f}/3")

    print("\n══════════════ 🤖 IA RECOMENDA ═════════════")
    print(f"💡 {gerar_recomendacao()}")
    print("\n══════════════ 📚 ESTUDOS ══════════════")
    print("1  - Python")
    print("2  - Algoritmos")
    print("3  - Banco de Dados")
    print("4  - Redes")
    print("5  - Inteligência Artificial")

    print("\n══════════════ 🚀 EVOLUÇÃO ══════════════")
    print("6  - Projetos")
    print("7  - Carreira em TI")
    print("8  - Exercícios")
    print("9  - Meu Plano de Estudos")

    print("\n══════════════ 📈 RELATÓRIOS ══════════════")
    print("10 - Ver Planos Salvos")
    print("11 - Quiz de Python")
    print("12 - Histórico de Desempenho")
    print("13 - Ver Conquistas")
    print("14 - Relatório Completo")
    print("15 - Desempenho por Matéria")

    print("\n══════════════ SISTEMA ══════════════")
    print("0  - Sair")
    print(LINHA)