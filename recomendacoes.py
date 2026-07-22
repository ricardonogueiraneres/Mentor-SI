from repositorio import (
    buscar_total_quizzes,
    buscar_xp,
    buscar_streak
)


def gerar_recomendacao():
    """
    Analisa os dados do aluno e retorna
    uma recomendação personalizada.
    """

    xp = buscar_xp()
    quizzes = buscar_total_quizzes()
    streak, _ = buscar_streak()

    # Pouca experiência
    if quizzes == 0:
        return "Faça seu primeiro quiz para medir seus conhecimentos."

    # XP baixo
    if xp < 100:
        return "Continue estudando Python básico antes de avançar."

    # Sequência interrompida
    if streak == 0:
        return "Estude hoje para iniciar uma nova sequência."

    # Boa evolução
    if xp >= 250:
        return "Excelente evolução! Comece um projeto prático."

    # Recomendação padrão
    return "Continue estudando um pouco todos os dias."