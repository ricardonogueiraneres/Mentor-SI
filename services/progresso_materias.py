from database.repositorio import (
    listar_materias_semestre,
    buscar_desempenho_por_materia,
)


def obter_progresso_materias(usuario_id: int) -> dict:
    """
    Retorna o progresso real das matérias
    cadastradas no semestre atual do aluno.
    """

    materias_semestre = listar_materias_semestre(usuario_id)

    progresso = {}

    for materia in materias_semestre:
        progresso[materia["nome"]] = materia["progresso"]

    return progresso

from database.repositorio import (
    listar_materias_semestre,
    atualizar_progresso_materia,
)

from xp import adicionar_xp
from conquistas import desbloquear

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

            if progresso == 100 and materia_selecionada["progresso"] < 100:

                novo_xp = adicionar_xp(usuario_id, 100)

                print("\n🎉 MATÉRIA CONCLUÍDA!")
                print("🏆 +100 XP")
                print(f"⭐ XP atual: {novo_xp}")

                desbloquear(
                    usuario_id,
                    f"Matéria concluída: {materia_selecionada['nome']}"
                )

        else:
            print("\n❌ Opção inválida.")

def calcular_progresso_semestre(materias_semestre) -> int:
    """
    Calcula o progresso médio das matérias do semestre.
    """

    if not materias_semestre:
        return 0

    total = sum(
        materia["progresso"]
        for materia in materias_semestre
    )

    return int(total / len(materias_semestre))