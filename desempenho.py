from database.repositorio import buscar_desempenho_por_materia

LINHA = "────────────────────────────────────────────"

def barra(percentual: int) -> str:
    """
    Gera uma barra de progresso baseada no percentual informado.
    """

    percentual = max(0, min(percentual, 100))
    cheios = percentual // 10

    return "█" * cheios + "░" * (10 - cheios)

def mostrar_desempenho(usuario_id):
    """
    Exibe o desempenho do aluno por matéria.
    """

    dados = buscar_desempenho_por_materia(usuario_id)

    print()

    print("╔══════════════════════════════════════════════════════╗")
    print("║          📚 DESEMPENHO POR MATÉRIA                  ║")
    print("╚══════════════════════════════════════════════════════╝")

    if not dados:

        print("\nNenhum quiz realizado ainda.")
        return

    print()

    for materia, quizzes, acertos, perguntas, media in dados:

        percentual = round((acertos / perguntas) * 100) if perguntas else 0

        print(f"📘 {materia}")

        print(f"📊 Aproveitamento.... {barra(percentual)} {percentual}%")

        print(f"🧠 Quizzes.......... {quizzes}")

        print(f"🎯 Acertos.......... {acertos}/{perguntas}")

        print(f"📈 Média............ {media:.1f}")

        print(LINHA)

    print()