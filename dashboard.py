from datetime import datetime
from services.recomendacao_service import gerar_recomendacao
from config import VERSAO, LINHA


def desenhar_barra(percentual: int) -> str:
    preenchido = percentual // 10
    vazio = 10 - preenchido
    return "█" * preenchido + "░" * vazio

def mostrar_dashboard(
    usuario_id: int,
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
    objetivo: str,
    progresso_materias: dict,
    proximo_desafio: str,
    meta_semanal: str,
    semestre,
    materias_semestre,
    progresso_semestre,
) -> None:
    """
    Exibe o painel principal do Mentor SI.
    """

    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print(f"║                  🎓 MENTOR SI {VERSAO}                  ║")
    print("║             Seu Professor de TI com IA              ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║ 📅 {agora:<47} ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    print("══════════════ 👤 PERFIL ══════════════")
    print(f"👤 Aluno............... {nome}")

    texto = "dia" if streak == 1 else "dias"
    print(f"🔥 Sequência........... {streak} {texto}")

    print(f"🎯 Objetivo............ {objetivo if objetivo else 'Não definido'}")
    print(f"🎖️ Rank................ {rank}")
    print(f"🏆 Nível............... {nivel}")

    if semestre:
        print("\n══════════════ 🎓 MEU SEMESTRE ══════════════")
        print(f"🏫 {semestre['faculdade']}")
        print(f"🎓 {semestre['curso']}")
        print(f"📚 {semestre['semestre']}º Semestre")

    if materias_semestre:
        print("\n══════════════ 📚 MATÉRIAS DO SEMESTRE ══════════════")

        for materia in materias_semestre:
            print(
                f"📘 {materia['nome']} "
                f"({materia['progresso']}%)"
            )

    print(
        f"\n📊 Progresso geral do semestre: "
        f"{progresso_semestre}%"
    )

    print("\n══════════════ ⭐ PROGRESSO ═════════════")

    print(f"⭐ XP Atual............. {xp}")
    print(f"📈 Evolução............ {barra}")
    print(f"📊 Progresso........... {porcentagem}%")
    print(f"🎯 Próximo nível....... {limite} XP")

    print("\n══════════════ 📊 ESTATÍSTICAS ═════════════")
    print(f"🧠 Quizzes............ {quizzes}")
    print(f"🏅 Conquistas......... {total_conquistas}")
    print(f"📈 Média Geral........ {media:.1f}/3")

    print("\n══════════════ 📚 PROGRESSO POR MATÉRIA ═════════════")

    icones = {
        "Python": "🐍",
        "Algoritmos": "🧠",
        "Banco de Dados": "🗄",
        "Redes": "🌐",
        "Inteligência Artificial": "🤖",
    }

    for materia, percentual in progresso_materias.items():
        barra_materia = desenhar_barra(percentual)
        icone = icones.get(materia, "📘")
        print(f"{icone} {materia:<24} {barra_materia} {percentual}%")

    print("\n══════════════ 🤖 IA RECOMENDA ═════════════")
    print("💡 Dica de hoje:")
    print(f"   ➜ {gerar_recomendacao(usuario_id)}")

    print("\n══════════════ 🤖 AI COACH ═════════════")

    print("💬 Recomendações para você")

    print("\n🚀 Próximo desafio:")
    print(f"   ➜ {proximo_desafio}")

    print("\n📅 Meta da semana:")
    print(f"   ➜ {meta_semanal}")

    print("\n" + "═" * 54)
    print("              MENU PRINCIPAL")
    print("═" * 54)

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
    print("16 - Objetivo Profissional")
    print("17 - AI Coach")
    print("18 - Roadmap para o Primeiro Emprego")
    print("19 - Cadastrar Meu Semestre")
    print("20 - Ver Meu Semestre")
    print("21 - Gerenciar Progresso das Matérias")

    print("\n══════════════ SISTEMA ══════════════")
    print("0  - Sair")

    print("\n💻 Continue evoluindo um código por dia!")

    print(LINHA)