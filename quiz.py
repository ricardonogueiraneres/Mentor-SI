from datetime import datetime
from xp import adicionar_xp
from missoes import concluir_missao
from conquistas import desbloquear
from repositorio import salvar_quiz

XP_QUIZ = 20
XP_BONUS = 10
TOTAL_PERGUNTAS = 3
MATERIA = "Python"


def fazer_pergunta(
    pergunta: str,
    alternativas: list[str],
    resposta_correta: str,
) -> int:
    """
    Exibe uma pergunta, recebe a resposta do usuário
    e retorna 1 em caso de acerto ou 0 em caso de erro.
    """

    print()
    print(pergunta)

    for alternativa in alternativas:
        print(alternativa)

    resposta = input("\nSua resposta: ").upper()

    if resposta == resposta_correta:

        print("\n✅ Correto!")
        return 1

    print("\n❌ Errado!")
    print(f"Resposta correta: {resposta_correta}")
    return 0


def quiz_python() -> None:
    """
    Executa o quiz de Python, registra o resultado,
    concede XP e verifica missões e conquistas.
    """

    pontos = 0

    print(f"\n===== QUIZ DE {MATERIA.upper()} =====")

    pontos += fazer_pergunta(

        "1) Qual comando adiciona um item em uma lista?",

        [
            "A) add()",
            "B) append()",
            "C) insert()"
        ],

        "B"
    )

    pontos += fazer_pergunta(

        "2) O que a função len() faz?",

        [
            "A) Remove itens da lista",
            "B) Conta a quantidade de elementos",
            "C) Ordena a lista"
        ],

        "B"
    )

    pontos += fazer_pergunta(

        "3) Qual é o índice do primeiro elemento de uma lista?",

        [
            "A) 1",
            "B) 0",
            "C) -1"
        ],

        "B"
    )

    print("\n======================")
    print("QUIZ FINALIZADO")
    print("======================")
    print(f"Sua pontuação foi: {pontos}/{TOTAL_PERGUNTAS}")

    # XP por concluir o quiz
    xp = adicionar_xp(XP_QUIZ)

    print(f"\n🎉 Você ganhou +{XP_QUIZ} XP!")

    # Bônus por acertar todas
    if pontos == TOTAL_PERGUNTAS:
        xp = adicionar_xp(XP_BONUS)
        print(f"🏅 Bônus de +{XP_BONUS} XP por acertar tudo!")

    print(f"⭐ XP Atual: {xp}")
    
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    salvar_quiz(
        materia=MATERIA,
        pontuacao=pontos,
        total=TOTAL_PERGUNTAS,
        data=agora
    )

    concluir_missao("quiz")
    
    desbloquear("Primeiro Quiz")