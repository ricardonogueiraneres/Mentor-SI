from database.repositorio import buscar_desempenho_por_materia


def obter_progresso_materias(usuario_id: int) -> dict:
    """
    Calcula o progresso de cada matéria com base nos quizzes realizados.
    """

    materias = {
        "Python": 0,
        "Algoritmos": 0,
        "Banco de Dados": 0,
        "Redes": 0,
        "Inteligência Artificial": 0,
    }

    desempenho = buscar_desempenho_por_materia(usuario_id)

    for materia, quizzes, acertos, perguntas, media in desempenho:

        if perguntas and perguntas > 0:
            percentual = int((acertos / perguntas) * 100)
        else:
            percentual = 0

        materias[materia] = percentual

    return materias