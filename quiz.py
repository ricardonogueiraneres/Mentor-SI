from services.quiz_service import finalizar_quiz
from config import XP_QUIZ, XP_BONUS
import xp

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


def quiz_python(usuario_id: int) -> None:
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
    xp, ganhou_bonus = finalizar_quiz(
        usuario_id=usuario_id,
        materia=MATERIA,
        pontos=pontos,
        total=TOTAL_PERGUNTAS,
        xp_quiz=XP_QUIZ,
        xp_bonus=XP_BONUS,
    )

    print(f"\n🎉 Você ganhou +{XP_QUIZ} XP!")

    if ganhou_bonus:
        print(f"🏅 Bônus de +{XP_BONUS} XP por acertar tudo!")
    print(f"⭐ XP Atual: {xp}")