from database.repositorio import (
    buscar_xp,
    buscar_total_quizzes,
    buscar_media_quizzes,
    buscar_total_conquistas,
    buscar_objetivo_profissional
)
import xp


def gerar_feedback(usuario_id):

    xp = buscar_xp(usuario_id)
    quizzes = buscar_total_quizzes(usuario_id)
    media = buscar_media_quizzes(usuario_id)
    conquistas = buscar_total_conquistas(usuario_id)
    objetivo = buscar_objetivo_profissional(usuario_id)

    feedback = []

    # XP
    if xp < 100:
        feedback.append(
            "📘 Você ainda está construindo sua base em programação."
        )

    elif xp < 300:
        feedback.append(
            "📈 Seu progresso é consistente. Continue resolvendo exercícios."
        )

    else:
        feedback.append(
            "🚀 Excelente evolução! Está na hora de desenvolver projetos completos."
        )

    # Quizzes
    if quizzes < 5:
        feedback.append(
            "📝 Faça mais quizzes para reforçar seu aprendizado."
        )

    else:
        feedback.append(
            "✅ Você está praticando regularmente através dos quizzes."
        )

    # Média
    if media >= 80:
        feedback.append(
            "🏆 Sua média é excelente."
        )

    elif media >= 60:
        feedback.append(
            "👍 Sua média é boa, mas ainda pode melhorar."
        )

    else:
        feedback.append(
            "📚 Revise os conteúdos antes de avançar."
        )

    # Objetivo profissional
    if objetivo:
        feedback.append(
            f"🎯 Objetivo profissional: {objetivo}"
        )

    else:
        feedback.append(
            "🎯 Defina um objetivo profissional para receber recomendações mais precisas."
        )

    # Conquistas
    feedback.append(
        f"🏅 Conquistas desbloqueadas: {conquistas}"
    )

    # Próximo desafio
    if objetivo == "Back-end":
        proximo_desafio = "Criar uma API REST em Python utilizando Flask."

    elif objetivo == "Front-end":
        proximo_desafio = "Desenvolver uma página responsiva com HTML, CSS e JavaScript."

    elif objetivo == "Inteligência Artificial":
        proximo_desafio = "Criar um chatbot utilizando a API do Gemini."

    elif objetivo == "Ciência de Dados":
        proximo_desafio = "Analisar um conjunto de dados utilizando Pandas."

    elif objetivo == "Redes":
        proximo_desafio = "Montar uma rede no Cisco Packet Tracer."

    elif objetivo == "Banco de Dados":
        proximo_desafio = "Criar um banco de dados relacional com PostgreSQL."

    elif objetivo == "Segurança da Informação":
        proximo_desafio = "Montar um laboratório de segurança utilizando Linux."

    else:
        proximo_desafio = "Defina um objetivo profissional para receber desafios personalizados."


    # Meta semanal
    if xp < 100:
        meta_semanal = (
            "Resolver 15 exercícios e concluir 2 quizzes."
        )

    elif xp < 300:
        meta_semanal = (
            "Criar um pequeno projeto e concluir 3 quizzes."
        )

    else:
        meta_semanal = (
            "Publicar um projeto no GitHub e concluir 5 quizzes."
        )


    # Mensagem motivacional
    if xp < 100:
        mensagem_final = (
            "💪 Todo profissional começou do zero. Continue praticando!"
        )

    elif xp < 300:
        mensagem_final = (
            "🚀 Você está evoluindo rapidamente. Continue mantendo sua rotina."
        )

    else:
        mensagem_final = (
            "🔥 Você já possui uma ótima base. Invista em projetos de portfólio."
        )


    return {
        "feedback": feedback,
        "proximo_desafio": proximo_desafio,
        "meta_semanal": meta_semanal,
        "mensagem_final": mensagem_final
    }

def mostrar_feedback(usuario_id):

    dados = gerar_feedback(usuario_id)

    print("\n╔══════════════════════════════════════════════╗")
    print("║               🤖 AI COACH                   ║")
    print("╚══════════════════════════════════════════════╝")

    print("\nSeu mentor analisou seu desempenho:")

    for mensagem in dados["feedback"]:
        print(f"\n{mensagem}")

    print("\n🚀 Próximo desafio:")
    print(dados["proximo_desafio"])

    print("\n📅 Meta da semana:")
    print(dados["meta_semanal"])

    print("\n" + dados["mensagem_final"])