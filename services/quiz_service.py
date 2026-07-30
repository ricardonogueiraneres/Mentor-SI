from datetime import datetime

from xp import adicionar_xp
from missoes import concluir_missao
from conquistas import desbloquear
from database.repositorio import salvar_quiz


def finalizar_quiz(
    usuario_id: int,
    materia: str,
    pontos: int,
    total: int,
    xp_quiz: int,
    xp_bonus: int,
) -> tuple[int, bool]:
    """
    Finaliza o quiz:
    - adiciona XP;
    - aplica bônus (se houver);
    - salva o resultado;
    - conclui missão;
    - desbloqueia conquista.

    Retorna:
        (xp_atual, ganhou_bonus)
    """

    xp = adicionar_xp(usuario_id, xp_quiz)

    ganhou_bonus = False

    if pontos == total:
        xp = adicionar_xp(usuario_id, xp_bonus)
        ganhou_bonus = True

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    salvar_quiz(
        usuario_id=usuario_id,
        materia=materia,
        pontuacao=pontos,
        total=total,
        data=agora,
    )

    concluir_missao(
        usuario_id,
        "quiz"
    )

    desbloquear(
        usuario_id,
        "Primeiro Quiz"
    )

    return xp, ganhou_bonus