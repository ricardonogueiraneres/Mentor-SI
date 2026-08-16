from database.repositorio import (
    listar_materias_semestre,
    atualizar_progresso_materia,
)


def gerenciar_progresso_materias(usuario_id: int):
    """
    Permite visualizar e atualizar o progresso
    das matérias do semestre.
    """

    while True:

        materias = listar_materias_semestre(usuario_id)

        print("\n══════════════ 📚 PROGRESSO DAS MATÉRIAS ══════════════")

        if not materias:
            print("\nNenhuma matéria cadastrada.")
            return

        for materia in materias:
            status = "✅" if materia["concluida"] else "📘"

            print(
                f"{status} {materia['id']} - "
                f"{materia['nome']} "
                f"({materia['progresso']}%)"
            )

        print("\n1 - Atualizar progresso")
        print("0 - Voltar")

        opcao = input("\nEscolha: ").strip()

        if opcao == "0":
            return

        if opcao == "1":

            try:
                materia_id = int(
                    input("\nDigite o ID da matéria: ")
                )

                materia_selecionada = next(
                    (
                        materia
                        for materia in materias
                        if materia["id"] == materia_id
                    ),
                    None
                )

                if materia_selecionada is None:
                    print("\n❌ Matéria não encontrada.")
                    continue

                progresso = int(
                    input("Digite o progresso (0-100): ")
                )

            except ValueError:
                print("\n❌ Digite apenas números.")
                continue

            if progresso < 0 or progresso > 100:
                print("\n❌ O progresso deve estar entre 0 e 100.")
                continue

            atualizar_progresso_materia(
                materia_id,
                progresso
            )

            print("\n✅ Progresso atualizado com sucesso!")

        else:
            print("\n❌ Opção inválida.")