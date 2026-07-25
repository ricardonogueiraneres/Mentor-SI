from database.repositorio import buscar_historico_quizzes

LINHA = "────────────────────────────────────────────"



def mostrar_historico(usuario_id: int) -> None:
    """
    Exibe o histórico dos quizzes realizados pelo aluno.
    """


    historico = buscar_historico_quizzes(usuario_id)

    print("\n╔══════════════════════════════════════════════════════╗")
    print("║             📚 HISTÓRICO DE DESEMPENHO              ║")
    print("╚══════════════════════════════════════════════════════╝")

    if not historico:
        print("\nNenhum quiz realizado ainda.")
        return

    for i, (data, materia, pontuacao, total) in enumerate(historico, start=1):

        print(f"\n📖 Quiz #{i}")
        print(f"📅 Data............. {data}")
        print(f"📘 Matéria.......... {materia}")
        print(f"🎯 Pontuação........ {pontuacao}/{total}")
        print(LINHA)

    print()