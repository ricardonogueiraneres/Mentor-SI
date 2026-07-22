from repositorio import buscar_conquistas, salvar_conquista


CABECALHO = (
    "╔════════════════════════════════════╗\n"
    "║        🏆 CONQUISTAS              ║\n"
    "╚════════════════════════════════════╝"
)


def carregar_conquistas() -> list[str]:
    """
    Retorna a lista de conquistas salvas.
    """
    return buscar_conquistas()


def desbloquear(nome: str) -> None:
    """
    Desbloqueia uma conquista caso ela ainda não exista.
    """

    conquistas = carregar_conquistas()

    if nome not in conquistas:
        salvar_conquista(nome)

        print("\n🏆 NOVA CONQUISTA DESBLOQUEADA!")
        print(f"⭐ {nome}")

             
def mostrar_conquistas() -> None:
    """
    Exibe todas as conquistas do aluno.
    """

    conquistas = carregar_conquistas()

    print(CABECALHO)
    
    if not conquistas:
        print("Nenhuma conquista ainda.")
        return

    print(f"\nTotal de conquistas: {len(conquistas)}\n")

    for conquista in conquistas:
        print("⭐", conquista)