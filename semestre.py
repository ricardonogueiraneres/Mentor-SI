from database.repositorio import (
    salvar_semestre,
    salvar_materia,
)


def cadastrar_semestre(usuario_id):
    """
    Cadastra o semestre atual do aluno.
    """

    print("\n══════════════ MEU SEMESTRE ══════════════")

    faculdade = input("🏫 Faculdade: ").strip()

    curso = input("🎓 Curso: ").strip()

    modalidade = input(
        "💻 Modalidade (EAD, Presencial ou Semipresencial): "
    ).strip()

    while True:
        try:
            semestre = int(input("📚 Semestre: "))

            if semestre > 0:
                break

            print("Digite um semestre válido.")

        except ValueError:
            print("Digite apenas números.")

    semestre_id = salvar_semestre(
        usuario_id,
        faculdade,
        curso,
        modalidade,
        semestre
    )

    print("\nAgora informe as matérias do semestre.")
    print("Digite uma por linha.")
    print("Quando terminar, pressione ENTER sem digitar nada.\n")

    ordem = 1

    while True:

        materia = input(f"{ordem}ª matéria: ").strip()

        if not materia:
            break

        if len(materia) < 3:
            print("❌ Nome da matéria inválido.")
            continue

        salvar_materia(
            semestre_id,
            materia,
            ordem
        )

        ordem += 1

    print("\n✅ Semestre cadastrado com sucesso!")


from database.repositorio import (
    salvar_semestre,
    salvar_materia,
    buscar_semestre,
    listar_materias,
)


def ver_semestre(usuario_id):
    """
    Exibe o semestre atual do aluno.
    """

    semestre = buscar_semestre(usuario_id)

    if not semestre:
        print("\nNenhum semestre cadastrado.")
        return

    semestre_id = semestre["id"]

    materias = listar_materias(semestre_id)

    print("\n══════════════ MEU SEMESTRE ══════════════")

    print(f"\n🏫 Faculdade: {semestre['faculdade']}")
    print(f"🎓 Curso: {semestre['curso']}")
    print(f"💻 Modalidade: {semestre['modalidade']}")
    print(f"📚 Semestre: {semestre['semestre']}º")

    print("\n══════════════ MATÉRIAS ══════════════")

    for indice, materia in enumerate(materias, start=1):

        nome = materia["nome"]
        progresso = materia["progresso"]

        print(f"{indice}. {nome} ({progresso}%)")