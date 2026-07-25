from database.repositorio import (
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

    
def mostrar_relatorio(usuario_id: int):

    nome = buscar_nome(usuario_id)

    xp = buscar_xp(usuario_id)

    streak, _ = buscar_streak(usuario_id)

    quizzes = buscar_total_quizzes(usuario_id)

    conquistas = buscar_total_conquistas(usuario_id)

    planos = buscar_total_planos(usuario_id)

    missoes = buscar_total_missoes(usuario_id)

    acertos = buscar_total_acertos(usuario_id)

    perguntas = buscar_total_perguntas(usuario_id)

    media = buscar_media_quizzes(usuario_id)

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