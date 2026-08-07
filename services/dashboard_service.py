from conquistas import carregar_conquistas
from database.repositorio import buscar_objetivo_profissional
from services.ai_coach import gerar_feedback
from services.progresso_materias import obter_progresso_materias

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

from database.repositorio import (
    buscar_objetivo_profissional,
    buscar_semestre,
    listar_materias_semestre,
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

    semestre = buscar_semestre(usuario_id)

    materias_semestre = listar_materias_semestre(usuario_id)

    coach = gerar_feedback(usuario_id)

    progresso_materias = obter_progresso_materias(usuario_id)

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
        "semestre": semestre,
        "materias_semestre": materias_semestre,
        
        "objetivo": objetivo,
        "proximo_desafio": coach["proximo_desafio"],
        "meta_semanal": coach["meta_semanal"],
        "progresso_materias": progresso_materias,
    }