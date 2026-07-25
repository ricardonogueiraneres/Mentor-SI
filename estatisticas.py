from database.repositorio import (
    buscar_total_quizzes,
    buscar_media_quizzes,
)


def total_quizzes(usuario_id: int) -> int:
    return buscar_total_quizzes(usuario_id)


def media_quizzes(usuario_id: int) -> float:
    return buscar_media_quizzes(usuario_id)


def recomendacao(media: float) -> str:
    """
    Retorna uma recomendação de estudos com base na média do aluno.
    """

    if media < 1.5:
        return "📚 Recomendo revisar Python básico, listas e funções antes de avançar."

    if media < 2.5:
        return "💪 Você está evoluindo! Continue praticando exercícios diariamente."

    return "🚀 Excelente desempenho! Você já pode estudar projetos mais avançados e Inteligência Artificial."
    
def conquista(quizzes: int) -> str:
    """
    Retorna a conquista correspondente à quantidade de quizzes realizados.
    """

    if quizzes == 0:
        return "🎯 Faça seu primeiro Quiz!"

    if quizzes < 5:
        return "🌱 Iniciante"

    if quizzes < 10:
        return "🔥 Aprendiz Dedicado"

    if quizzes < 20:
        return "🏆 Mestre dos Quizzes"

    return "👑 Lenda do Mentor SI"

def nivel_aluno(media: float) -> str:
    """
    Classifica o aluno de acordo com a média dos quizzes.
    """

    if media < 1.5:
        return "Iniciante"

    if media < 2.5:
        return "Intermediário"

    return "Avançado"
    
