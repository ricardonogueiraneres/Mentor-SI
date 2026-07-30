from conquistas import carregar_conquistas
from database.repositorio import buscar_objetivo_profissional
from services.ai_coach import gerar_feedback

from estatisticas import (
    total_quizzes,
    media_quizzes,
    nivel_aluno,
)

from streak import atualizar_streak

from xp import (
    carregar_xp,
    barra_xp,
    nivel_xp,
)


def obter_dashboard(usuario_id: int) -> dict:
    """
    Monta todos os dados necessários para exibir o dashboard.
    """

    quizzes = total_quizzes(usuario_id)
    xp = carregar_xp(usuario_id)

    barra, porcentagem, limite = barra_xp(xp)

    media = media_quizzes(usuario_id)
    nivel = nivel_aluno(media)
    rank = nivel_xp(xp)

    streak = atualizar_streak(usuario_id)

    conquistas = carregar_conquistas(usuario_id)

    objetivo = buscar_objetivo_profissional(usuario_id)

    coach = gerar_feedback(usuario_id)

    return {
        "quizzes": quizzes,
        "xp": xp,
        "barra": barra,
        "porcentagem": porcentagem,
        "limite": limite,
        "media": media,
        "nivel": nivel,
        "rank": rank,
        "streak": streak,
        "total_conquistas": len(conquistas),
        
        "objetivo": objetivo,
        "proximo_desafio": coach["proximo_desafio"],
        "meta_semanal": coach["meta_semanal"],
    }