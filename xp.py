from repositorio import buscar_xp, atualizar_xp


def carregar_xp(usuario_id: int) -> int:
    """
    Retorna o XP do usuário informado.
    """
    return buscar_xp(usuario_id)


def salvar_xp(usuario_id: int, xp: int) -> None:
    """
    Salva o XP do usuário.
    """
    atualizar_xp(usuario_id, xp)


def adicionar_xp(usuario_id: int, valor: int) -> int:
    """
    Adiciona XP ao usuário e salva o novo valor.
    """
    xp = carregar_xp(usuario_id)

    xp += valor

    salvar_xp(usuario_id, xp)

    return xp


def nivel_xp(xp: int) -> str:
    """
    Retorna o nível correspondente ao XP informado.
    """

    if xp < 100:
        return "🌱 Iniciante"

    if xp < 250:
        return "📘 Aprendiz"

    if xp < 500:
        return "🥈 Intermediário"

    if xp < 1000:
        return "🥇 Avançado"

    if xp < 2000:
        return "🏆 Especialista"

    return "👑 Mestre Mentor"


def barra_xp(xp: int) -> tuple[str, int, int]:
    """
    Gera a barra de progresso do XP.
    """

    if xp < 100:
        limite = 100

    elif xp < 250:
        limite = 250

    elif xp < 500:
        limite = 500

    elif xp < 1000:
        limite = 1000

    else:
        limite = 2000

    porcentagem = min(int((xp / limite) * 100), 100)

    barras = porcentagem // 10

    barra = "█" * barras + "░" * (10 - barras)

    return barra, porcentagem, limite