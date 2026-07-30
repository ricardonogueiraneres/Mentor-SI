from database.repositorio import (
    salvar_objetivo_profissional,
    buscar_objetivo_profissional
)

OPCOES = {
    1: "Back-end",
    2: "Front-end",
    3: "Inteligência Artificial",
    4: "Ciência de Dados",
    5: "Redes",
    6: "Banco de Dados",
    7: "Segurança da Informação"
}


def definir_objetivo(usuario_id):

    print("\n==============================")
    print("🎯 OBJETIVO PROFISSIONAL")
    print("==============================")

    for codigo, nome in OPCOES.items():
        print(f"{codigo} - {nome}")

    while True:
        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao in OPCOES:
                break

            print("Escolha uma opção válida.")

        except ValueError:
            print("Digite apenas números.")

    objetivo = OPCOES[opcao]

    salvar_objetivo_profissional(usuario_id, objetivo)

    print("\n✅ Objetivo salvo com sucesso!")
    print(f"🎯 Seu objetivo agora é: {objetivo}")


def mostrar_objetivo(usuario_id):

    objetivo = buscar_objetivo_profissional(usuario_id)

    if objetivo:
        print(f"\n🎯 Objetivo atual: {objetivo}")
    else:
        print("\nNenhum objetivo profissional foi definido.")