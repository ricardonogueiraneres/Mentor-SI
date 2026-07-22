from repositorio import buscar_nome, salvar_usuario


def carregar_perfil() -> str:
    """
    Carrega o nome do usuário.
    Caso ainda não exista, solicita o cadastro
    e salva no banco de dados.
    """

    nome = buscar_nome()

    if nome:
        return nome

    while True:
        nome = input("\n👤 Digite seu nome: ").strip()

        if nome:
            break

        print("❌ O nome não pode ficar vazio.")

    salvar_usuario(nome)

    return nome