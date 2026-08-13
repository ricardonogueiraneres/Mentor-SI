from database.repositorio import (
    buscar_xp,
    buscar_total_quizzes,
    buscar_media_quizzes,
    buscar_total_conquistas,
    buscar_objetivo_profissional,
    buscar_semestre,
    listar_materias_semestre,
    buscar_ultimo_plano,
)


def escolher_materia_prioritaria(materias_semestre):
    """
    Escolhe a matéria que precisa de mais atenção.
    """

    if not materias_semestre:
        return None

    materias_pendentes = [
        materia
        for materia in materias_semestre
        if materia["concluida"] == 0
    ]

    if not materias_pendentes:
        return None

    return min(
        materias_pendentes,
        key=lambda materia: materia["progresso"]
    )

def gerar_feedback(usuario_id):

    xp = buscar_xp(usuario_id)
    quizzes = buscar_total_quizzes(usuario_id)
    media = buscar_media_quizzes(usuario_id)
    conquistas = buscar_total_conquistas(usuario_id)
    objetivo = buscar_objetivo_profissional(usuario_id)
    semestre = buscar_semestre(usuario_id)
    materias_semestre = listar_materias_semestre(usuario_id)
    plano = buscar_ultimo_plano(usuario_id)

    materia_prioritaria = escolher_materia_prioritaria(
        materias_semestre
    )

    motivo_prioridade = None

    if materia_prioritaria:

        progresso = materia_prioritaria["progresso"]
        nome_materia = materia_prioritaria["nome"]

        motivo_prioridade = (
            f"A matéria '{nome_materia}' está com "
            f"{progresso}% de progresso e precisa de mais atenção."
        )

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
    if materia_prioritaria:

        nome_materia = materia_prioritaria["nome"]
        progresso = materia_prioritaria["progresso"]

        proximo_desafio = (
            f"Estudar '{nome_materia}' "
            f"({progresso}% de progresso) "
            f"e realizar um exercício para fixar o conteúdo."
        )

    elif objetivo == "Back-end":

        proximo_desafio = (
            "Criar uma API REST em Python utilizando Flask."
        )

    elif objetivo == "Front-end":

        proximo_desafio = (
            "Desenvolver uma página responsiva "
            "com HTML, CSS e JavaScript."
        )

    elif objetivo == "Inteligência Artificial":

        proximo_desafio = (
            "Criar um chatbot utilizando a API do Gemini."
        )

    elif objetivo == "Ciência de Dados":

        proximo_desafio = (
            "Analisar um conjunto de dados utilizando Pandas."
        )

    elif objetivo == "Redes":

        proximo_desafio = (
            "Montar uma rede no Cisco Packet Tracer."
        )

    elif objetivo == "Banco de Dados":

        proximo_desafio = (
            "Criar um banco de dados relacional com PostgreSQL."
        )

    elif objetivo == "Segurança da Informação":

        proximo_desafio = (
            "Montar um laboratório de segurança utilizando Linux."
        )

    else:

        proximo_desafio = (
            "Defina um objetivo profissional "
            "para receber desafios personalizados."
        )


    plano_diario = None

    if plano:
        horas = plano["horas"]

        if materia_prioritaria:
            nome_materia = materia_prioritaria["nome"]

            if horas >= 2:

                segunda_materia = None

                for materia in materias_semestre:
                    if (
                        materia["nome"] != nome_materia
                        and materia["concluida"] == 0
                    ):
                        segunda_materia = materia["nome"]
                        break

                if segunda_materia:

                    plano_diario = (
                        f"📘 {nome_materia}: 60 minutos\n"
                        f"🧠 {segunda_materia}: 40 minutos\n"
                        "📝 Quiz: 20 minutos"
                    )

                else:

                    plano_diario = (
                        f"📘 {nome_materia}: 90 minutos\n"
                        "📝 Quiz: 30 minutos"
                    )

            elif horas == 1:

                plano_diario = (
                    f"📘 {nome_materia}: 40 minutos\n"
                    "📝 Quiz: 20 minutos"
                )

            else:

                plano_diario = (
                    f"📘 {nome_materia}: 30 minutos\n"
                    "📝 Revisão: 15 minutos"
                )

    # Meta semanal

    if materias_semestre:

        materias_pendentes = [
            materia
            for materia in materias_semestre
            if materia["concluida"] == 0
        ]

        if materias_pendentes:

            materia_1 = materias_pendentes[0]["nome"]

            if len(materias_pendentes) > 1:

                materia_2 = materias_pendentes[1]["nome"]

                meta_semanal = (
                    f"Estudar '{materia_1}', "
                    f"revisar '{materia_2}' "
                    f"e concluir 2 quizzes."
                )

            else:

                meta_semanal = (
                    f"Estudar '{materia_1}' "
                    f"e concluir 2 quizzes."
                )

        else:

            meta_semanal = (
                "Revisar as matérias concluídas "
                "e realizar 3 quizzes."
            )

    else:

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
            "🚀 Você está evoluindo rapidamente. "
            "Continue mantendo sua rotina."
        )

    else:

        mensagem_final = (
            "🔥 Você já possui uma ótima base. "
            "Invista em projetos de portfólio."
        )

    # Contexto acadêmico

    if semestre:

        feedback.append(
            f"🎓 Você está no {semestre['semestre']}º semestre "
            f"de {semestre['curso']}."
        )

    if materias_semestre:

        feedback.append(
            "📚 Matérias atuais: "
            + ", ".join(
                materia["nome"]
                for materia in materias_semestre
            )
        )

    return {
        "feedback": feedback,
        "proximo_desafio": proximo_desafio,
        "meta_semanal": meta_semanal,
        "mensagem_final": mensagem_final,
        "motivo_prioridade": motivo_prioridade,
        "plano_diario": plano_diario,
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

    if dados["motivo_prioridade"]:

        print("\n💡 Por que essa matéria?")
        print(dados["motivo_prioridade"])

    if dados["plano_diario"]:

        print("\n⏱️ Plano de estudo de hoje:")
        print(dados["plano_diario"])

    print("\n📅 Meta da semana:")
    print(dados["meta_semanal"])

    print("\n" + dados["mensagem_final"])