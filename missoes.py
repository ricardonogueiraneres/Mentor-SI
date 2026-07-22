from datetime import datetime

from repositorio import (
    buscar_missoes,
    atualizar_missao
)


def mostrar_missoes():

    hoje = datetime.now().strftime("%d/%m/%Y")

    missoes = buscar_missoes(hoje)

    print("\n==========================")
    print("📅 MISSÕES DE HOJE")
    print("==========================")

    print(f"{'✅' if missoes['ia'] else '⬜'} Conversar com a IA")
    print(f"{'✅' if missoes['quiz'] else '⬜'} Fazer um Quiz")
    print(f"{'✅' if missoes['plano'] else '⬜'} Criar Plano de Estudos")

    concluidas = sum(missoes.values())

    porcentagem = int((concluidas / 3) * 100)

    print("--------------------------")
    print(f"📈 Progresso: {concluidas}/3 ({porcentagem}%)")


def concluir_missao(nome):

    hoje = datetime.now().strftime("%d/%m/%Y")

    missoes = buscar_missoes(hoje)

    if not missoes[nome]:

        atualizar_missao(hoje, nome)

        print(f"\n🎯 Missão '{nome}' concluída!")