from database.repositorio import buscar_desempenho_por_materia

PESOS = {
    "progresso": 50,
    "quiz": 30,
    "objetivo": 20,
}

OBJETIVOS = {
    "Back-end": {
        "Algoritmos",
        "Algoritmos e Estruturas de Dados",
        "Banco de Dados",
        "Python",
    },
    "Front-end": {"Python"},
    "Inteligência Artificial": {"Python"},
    "Redes": {"Redes"},
    "Banco de Dados": {"Banco de Dados"},
}


def calcular_prioridade(materias, usuario_id, objetivo):
    desempenho = buscar_desempenho_por_materia(usuario_id)

    medias = {}

    for materia, _, acertos, perguntas, _ in desempenho:
        if perguntas:
            medias[materia] = int((acertos / perguntas) * 100)

    ranking = []

    for materia in materias:

        nome = materia["nome"]
        progresso = materia["progresso"]

        score = 0

        # Quanto menor o progresso, maior a prioridade
        score += (100 - progresso) * 0.5

        quiz = medias.get(nome, 0)
        score += (100 - quiz) * 0.3

        if objetivo in OBJETIVOS and nome in OBJETIVOS[objetivo]:
            score += 20

        ranking.append({
            "nome": nome,
            "progresso": progresso,
            "quiz": quiz,
            "score": round(score, 1),
        })

    ranking.sort(key=lambda x: x["score"], reverse=True)

    return ranking