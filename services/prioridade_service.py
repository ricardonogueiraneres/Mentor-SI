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
    "Front-end": {
        "Python",
    },
    "Inteligência Artificial": {
        "Python",
    },
    "Redes": {
        "Redes",
    },
    "Banco de Dados": {
        "Banco de Dados",
    },
}


def classificar_prioridade(score):
    """
    Classifica a prioridade com base no score final.
    """

    if score >= 70:
        return "ALTA", "🔴"

    if score >= 40:
        return "MÉDIA", "🟡"

    return "BAIXA", "🟢"


def calcular_prioridade(materias, usuario_id, objetivo):
    """
    Calcula o ranking de prioridade das matérias
    com base em:

    - progresso da matéria
    - desempenho nos quizzes
    - objetivo profissional
    """

    desempenho = buscar_desempenho_por_materia(usuario_id)

    medias = {}

    for materia, _, acertos, perguntas, _ in desempenho:

        if perguntas:
            medias[materia] = int(
                (acertos / perguntas) * 100
            )

    ranking = []

    for materia in materias:

        # Matérias concluídas não precisam
        # aparecer como prioridade de estudo.
        if materia["concluida"] == 1:
            continue

        nome = materia["nome"]
        progresso = materia["progresso"]

        score_progresso = (
            (100 - progresso)
            * (PESOS["progresso"] / 100)
        )

        quiz = medias.get(nome, 0)

        score_quiz = (
            (100 - quiz)
            * (PESOS["quiz"] / 100)
        )

        score_objetivo = 0

        if (
            objetivo in OBJETIVOS
            and nome in OBJETIVOS[objetivo]
        ):
            score_objetivo = PESOS["objetivo"]

        score = (
            score_progresso
            + score_quiz
            + score_objetivo
        )

        prioridade, icone = classificar_prioridade(score)

        motivos = []

        if progresso < 30:
            motivos.append(
                f"progresso muito baixo ({progresso}%)"
            )

        elif progresso < 70:
            motivos.append(
                f"progresso intermediário ({progresso}%)"
            )

        if quiz == 0:
            motivos.append(
                "ainda não possui desempenho em quizzes"
            )

        elif quiz < 60:
            motivos.append(
                f"baixo desempenho nos quizzes ({quiz}%)"
            )

        elif quiz >= 80:
            motivos.append(
                f"bom desempenho nos quizzes ({quiz}%)"
            )

        if (
            objetivo in OBJETIVOS
            and nome in OBJETIVOS[objetivo]
        ):
            motivos.append(
                f"está relacionada ao objetivo profissional "
                f"{objetivo}"
            )

        motivo = (
            "Prioridade definida porque "
            + ", ".join(motivos)
            + "."
        )

        ranking.append({
            "nome": nome,
            "progresso": progresso,
            "quiz": quiz,
            "score": round(score, 1),
            "prioridade": prioridade,
            "icone": icone,
            "motivo": motivo,
        })

    ranking.sort(
        key=lambda x: (-x["score"], x["progresso"], x["nome"])
    )

    return ranking