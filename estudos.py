from datetime import datetime

from repositorio import salvar_plano, listar_planos
from missoes import concluir_missao
from conquistas import desbloquear

FORMATO_DATA = "%d/%m/%Y %H:%M"
LINHA = "-" * 40


def plano_estudos() -> None:
    """
    Gera um plano de estudos personalizado e salva no banco.
    """

    while True:
        try:
            horas = int(input("Quantas horas por dia você pode estudar? "))

            if horas > 0:
                break

            print("Digite um número maior que zero.")

        except ValueError:
            print("Digite apenas números inteiros.")

    objetivo = input(
        "Seu objetivo é (Python, IA, Redes ou Banco de Dados)? "
    ).strip()

    print("\n===== PLANO DE ESTUDOS =====")

    if horas <= 1:
        print("Python: 20 minutos")
        print("Algoritmos: 20 minutos")
        print("IA: 20 minutos")

    elif horas <= 3:
        print("Python: 1 hora")
        print("Algoritmos: 30 minutos")
        print("Banco de Dados: 30 minutos")
        print("Redes: 30 minutos")
        print("IA: 30 minutos")

    else:
        print("Python: 1 hora")
        print("Algoritmos: 1 hora")
        print("Banco de Dados: 1 hora")
        print("Redes: 1 hora")
        print("IA: 1 hora")

    print(f"\nFoco principal: {objetivo}")
    print(f"Plano criado para {horas} horas de estudo por dia.")

    agora = datetime.now().strftime(FORMATO_DATA)

    salvar_plano(objetivo, horas, agora)

    concluir_missao("plano")
    desbloquear("Primeiro Plano de Estudos")


def ver_planos() -> None:
    """
    Exibe todos os planos de estudos cadastrados.
    """

    planos = listar_planos()

    print("\n===== PLANOS SALVOS =====")

    if not planos:
        print("Nenhum plano foi salvo ainda.")
        return

    for objetivo, horas, data in planos:
        print(f"📅 {data}")
        print(f"🎯 Objetivo: {objetivo}")
        print(f"⏰ Horas por dia: {horas}")
        print(LINHA)