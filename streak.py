from datetime import datetime
from repositorio import buscar_streak, atualizar_streak_bd

FORMATO_DATA = "%Y-%m-%d"


def carregar_streak(usuario_id: int) -> tuple[int, str]:
    """
    Retorna a sequência atual de estudos e a última data registrada.
    """
    return buscar_streak(usuario_id)


def salvar_streak(usuario_id: int, dias: int, data: str) -> None:
    """
    Salva a sequência de estudos e a data da última atividade.
    """
    atualizar_streak_bd(usuario_id, dias, data)


def atualizar_streak(usuario_id: int) -> int:
    """
    Atualiza a sequência de estudos do usuário
    com base na última data registrada.
    """

    hoje = datetime.now().date()
    data_hoje = hoje.strftime(FORMATO_DATA)

    dias, ultima_data = carregar_streak(usuario_id)

    if ultima_data == "":
        salvar_streak(usuario_id, 1, data_hoje)
        return 1

    ultima = datetime.strptime(ultima_data, FORMATO_DATA).date()

    diferenca = (hoje - ultima).days

    if diferenca == 0:
        return dias

    if diferenca == 1:
        dias += 1
        salvar_streak(usuario_id, dias, data_hoje)
        return dias

    salvar_streak(usuario_id, 1, data_hoje)
    return 1