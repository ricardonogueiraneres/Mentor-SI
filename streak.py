from datetime import datetime
from repositorio import buscar_streak, atualizar_streak_bd

FORMATO_DATA = "%Y-%m-%d"


def carregar_streak() -> tuple[int, str]:
    """
    Retorna a sequência atual de estudos e a última data registrada.
    """
    return buscar_streak()


def salvar_streak(dias: int, data: str) -> None:
    """
    Salva a sequência de estudos e a data da última atividade.
    """
    atualizar_streak_bd(dias, data)


def atualizar_streak() -> int:
    """
    Atualiza a sequência de estudos do usuário
    com base na última data registrada.
    """

    hoje = datetime.now().date()
    data_hoje = hoje.strftime(FORMATO_DATA)

    dias, ultima_data = carregar_streak()

    if ultima_data == "":

        salvar_streak(1, data_hoje)
        return 1

    ultima = datetime.strptime(ultima_data, FORMATO_DATA).date()

    diferenca = (hoje - ultima).days

    if diferenca == 0:
        return dias

    if diferenca == 1:
        dias += 1
        salvar_streak(dias, data_hoje)
        return dias

    salvar_streak(1, data_hoje)
    return 1
