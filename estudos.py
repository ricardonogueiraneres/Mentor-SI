from database.repositorio import salvar_plano, listar_planos
from missoes import concluir_missao
from conquistas import desbloquear
from datetime import datetime
from services.plano_inteligente import gerar_plano_inteligente

FORMATO_DATA = "%d/%m/%Y %H:%M"
LINHA = "-" * 40


def plano_estudos(usuario_id: int) -> None:
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

    agora = datetime.now().strftime(FORMATO_DATA)

    salvar_plano(usuario_id, objetivo, horas, agora)

    concluir_missao(usuario_id, "plano")
    
    desbloquear(usuario_id, "Primeiro Plano de Estudos")
    
    plano = gerar_plano_inteligente(usuario_id)

    print("\n╔══════════════════════════════════════════════╗")
    print("║      📚 PLANO INTELIGENTE DE ESTUDOS        ║")
    print("╚══════════════════════════════════════════════╝")

    print(f"\n⭐ XP: {plano['xp']}")
    print(f"🧠 Quizzes: {plano['quizzes']}")
    print(f"🏆 Conquistas: {plano['conquistas']}")

    print("\n🎯 Objetivo Profissional:")

    if plano["objetivo"]:
        print(plano["objetivo"])
    else:
        print("Não definido")

    print("\nHoje recomendamos:")

    print(f"🐍 Python ............. {plano['python']} min")
    print(f"🧩 Algoritmos ......... {plano['algoritmos']} min")
    print(f"💻 Projeto ............ {plano['projeto']} min")

    print("\n🤖 Mentor SI recomenda:")
    print(plano["mensagem"])

    print("\n📚 Recomendação Personalizada:")
    print(plano["recomendacao"])

    print("\n🎯 Próxima meta:")
    print(plano["meta"])

    if plano["objetivo"]:
        print(f"\n🎯 Objetivo Profissional: {plano['objetivo']}")
    else:
        print(f"\n🎯 Foco informado: {objetivo}")

    print(f"Plano criado para {horas} horas de estudo por dia.")

     
def ver_planos(usuario_id: int) -> None:
    """
    Exibe todos os planos de estudos cadastrados.
    """

    planos = listar_planos(usuario_id)   

    print("\n===== PLANOS SALVOS =====")

    if not planos:
        print("Nenhum plano foi salvo ainda.")
        return

    for objetivo, horas, data in planos:
        print(f"📅 {data}")
        print(f"🎯 Objetivo: {objetivo}")
        print(f"⏰ Horas por dia: {horas}")
        print(LINHA)