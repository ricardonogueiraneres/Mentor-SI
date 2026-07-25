from database.repositorio import buscar_conquistas, salvar_conquista


CABECALHO = (
    "╔════════════════════════════════════╗\n"
    "║        🏆 CONQUISTAS              ║\n"
    "╚════════════════════════════════════╝"
)


def carregar_conquistas(usuario_id: int) -> list[str]:
    """
    Retorna a lista de conquistas do usuário.
    """
    return buscar_conquistas(usuario_id)


def desbloquear(usuario_id: int, nome: str) -> None:
    """
    Desbloqueia uma conquista caso ela ainda não exista.
    """

    conquistas = carregar_conquistas(usuario_id)

    if nome not in conquistas:
        salvar_conquista(usuario_id, nome)

        print("\n🏆 NOVA CONQUISTA DESBLOQUEADA!")
        print(f"⭐ {nome}")


def mostrar_conquistas(usuario_id: int) -> None:
    """
    Exibe todas as conquistas do aluno.
    """

    conquistas = carregar_conquistas(usuario_id)

    print(CABECALHO)

    if not conquistas:
        print("Nenhuma conquista ainda.")
        return

    print(f"\nTotal de conquistas: {len(conquistas)}\n")

    for conquista in conquistas:
        print("⭐", conquista)