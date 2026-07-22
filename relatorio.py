from repositorio import (
    buscar_nome,
    buscar_xp,
    buscar_streak,
    buscar_total_quizzes,
    buscar_total_conquistas,
    buscar_total_planos,
    buscar_total_missoes,
    buscar_total_acertos,
    buscar_total_perguntas,
    buscar_media_quizzes
)

from xp import nivel_xp

    
def mostrar_relatorio():

    nome = buscar_nome()

    xp = buscar_xp()

    streak, _ = buscar_streak()

    quizzes = buscar_total_quizzes()

    conquistas = buscar_total_conquistas()

    planos = buscar_total_planos()

    missoes = buscar_total_missoes()

    acertos = buscar_total_acertos()

    perguntas = buscar_total_perguntas()

    media = buscar_media_quizzes()

    rank = nivel_xp(xp)

    print()

    print("╔══════════════════════════════════════════════════════╗")
    print("║             📊 RELATÓRIO MENTOR SI                  ║")
    print("╚══════════════════════════════════════════════════════╝")

    print()

    print("══════════════ 👤 PERFIL ══════════════")
    print(f"👤 Aluno............... {nome}")
    print(f"🏆 Nível............... {rank}")

    texto = "dia" if streak == 1 else "dias"
    print(f"🔥 Sequência........... {streak} {texto}")

    print()

    print("══════════════ 📊 DESEMPENHO ══════════════")
    print(f"⭐ XP.................. {xp}")
    print(f"🧠 Quizzes............ {quizzes}")
    print(f"🎯 Acertos............ {acertos}/{perguntas}")
    print(f"📈 Média.............. {media:.1f}/3")

    print()

    print("══════════════ 🏆 CONQUISTAS ══════════════")
    print(f"🏅 Conquistas......... {conquistas}")
    print(f"📝 Planos............. {planos}")
    print(f"🎯 Missões............ {missoes}")

    print()

    print("══════════════ 🤖 IA ANALISOU ══════════════")

    if quizzes == 0:
        print("💡 Faça seu primeiro quiz.")
    elif media < 2:
        print("💡 Revise Python antes de avançar.")
    elif xp >= 250:
        print("💡 Excelente evolução! Hora de criar projetos.")
    else:
        print("💡 Continue estudando diariamente.")

    print()

    print("══════════════════════════════════════════════════════")