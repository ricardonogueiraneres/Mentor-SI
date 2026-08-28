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

from services.prioridade_service import calcular_prioridade


def classificar_prioridade(progresso: int) -> tuple[str, str]:
    """
    Classifica a prioridade de estudo de acordo
    com o progresso da matéria.
    """

    if progresso >= 100:
        return "CONCLUÍDA", "✅"

    if progresso < 30:
        return "ALTA", "🔴"

    if progresso < 70:
        return "MÉDIA", "🟡"

    return "BAIXA", "🟢"


def escolher_materia_prioritaria(materias_semestre):
    """
    Escolhe a matéria que precisa de mais atenção
    e informa o motivo da prioridade.
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

    materia_prioritaria = min(
        materias_pendentes,
        key=lambda materia: (
            materia["progresso"],
            materia["id"]
        )
    )

    progresso = materia_prioritaria["progresso"]

    materias_com_mesmo_progresso = [
        materia
        for materia in materias_pendentes
        if materia["progresso"] == progresso
    ]

    if len(materias_com_mesmo_progresso) > 1:
        motivo = (
            f"Esta matéria está entre as que possuem menor "
            f"progresso ({progresso}%) no seu semestre."
        )
    else:
        motivo = (
            f"Esta é atualmente a matéria com menor progresso "
            f"do seu semestre ({progresso}%)."
        )

    prioridade, icone = classificar_prioridade(progresso)

    return {
        "materia": materia_prioritaria,
        "motivo": motivo,
        "prioridade": prioridade,
        "icone": icone,
    }


def gerar_meta_semanal(
    materia_prioritaria,
    materias_semestre
):
    """
    Cria uma meta semanal baseada nas matérias
    que ainda precisam ser concluídas.
    """

    if not materia_prioritaria:
        return "Revisar os conteúdos e concluir as matérias pendentes."

    nome_prioritaria = materia_prioritaria["materia"]["nome"]

    outras_materias = []

    for materia in materias_semestre:
        if (
            materia["nome"] != nome_prioritaria
            and materia["concluida"] == 0
        ):
            outras_materias.append(materia["nome"])

    if outras_materias:
        segunda_materia = outras_materias[0]

        return (
            f"Estudar '{nome_prioritaria}', "
            f"revisar '{segunda_materia}' "
            f"e concluir 2 quizzes."
        )

    return (
        f"Estudar '{nome_prioritaria}' "
        f"e concluir 2 quizzes."
    )


def gerar_plano_diario(
    plano,
    materia_prioritaria,
    materias_semestre
):
    """
    Cria o plano de estudo diário com base
    no tempo disponível e nas matérias pendentes.
    """

    if not plano or not materia_prioritaria:
        return None

    horas = plano["horas"]

    nome_prioritaria = materia_prioritaria["materia"]["nome"]

    segunda_materia = None

    for materia in materias_semestre:
        if (
            materia["nome"] != nome_prioritaria
            and materia["concluida"] == 0
        ):
            segunda_materia = materia["nome"]
            break

    # 2 horas ou mais
    if horas >= 2:

        if segunda_materia:
            return (
                f"📘 {nome_prioritaria}: 60 minutos\n"
                f"📚 {segunda_materia}: 30 minutos\n"
                "📝 Revisão e exercícios: 30 minutos"
            )

        return (
            f"📘 {nome_prioritaria}: 60 minutos\n"
            "📝 Revisão e exercícios: 30 minutos\n"
            "📚 Quiz: 30 minutos"
        )

    # Entre 1 e 2 horas
    if horas >= 1:

        if segunda_materia:
            return (
                f"📘 {nome_prioritaria}: 40 minutos\n"
                f"📚 {segunda_materia}: 20 minutos"
            )

        return (
            f"📘 {nome_prioritaria}: 40 minutos\n"
            "📝 Revisão e exercícios: 20 minutos"
        )

    # Menos de 1 hora
    return (
        f"📘 {nome_prioritaria}: 30 minutos\n"
        "📝 Revisão rápida e exercícios: 15 minutos"
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
    ranking = calcular_prioridade(
        materias_semestre,
        usuario_id,
        objetivo
    )

    materia_prioritaria = None

    if ranking:
        primeiro = ranking[0]

        prioridade, icone = classificar_prioridade(
            primeiro["progresso"]
        )

        materia = next(
            (
                materia
                for materia in materias_semestre
                if materia["nome"] == primeiro["nome"]
            ),
            None
        )

        if materia:
            materia_prioritaria = {
                "materia": materia,
                "motivo": (
                    f"Esta matéria recebeu a maior prioridade "
                    f"no ranking ({primeiro['score']} pontos), "
                    f"considerando progresso, desempenho nos quizzes "
                    f"e objetivo profissional."
                ),
                "prioridade": prioridade,
                "icone": icone,
            }

    motivo_prioridade = None
    prioridade = None
    icone_prioridade = None

    if materia_prioritaria:

        motivo_prioridade = materia_prioritaria["motivo"]
        prioridade = materia_prioritaria["prioridade"]
        icone_prioridade = materia_prioritaria["icone"]

    feedback = []

    # ==========================================================
    # XP
    # ==========================================================

    if xp < 100:

        feedback.append(
            "📘 Você ainda está construindo sua base em programação."
        )

    elif xp < 300:

        feedback.append(
            "📈 Seu progresso é consistente. "
            "Continue resolvendo exercícios."
        )

    else:

        feedback.append(
            "🚀 Excelente evolução! "
            "Está na hora de desenvolver projetos completos."
        )

    # ==========================================================
    # QUIZZES
    # ==========================================================

    if quizzes < 5:

        feedback.append(
            "📚 Continue realizando quizzes para reforçar seus conhecimentos."
        )

    elif media >= 80:

        feedback.append(
            "🏆 Sua média nos quizzes é excelente."
        )

    elif media >= 60:

        feedback.append(
            "👍 Sua média é boa, mas ainda pode melhorar."
        )

    else:

        feedback.append(
            "📚 Revise os conteúdos antes de avançar."
        )

    # ==========================================================
    # OBJETIVO PROFISSIONAL
    # ==========================================================

    if objetivo:

        feedback.append(
            f"🎯 Objetivo profissional: {objetivo}"
        )

    else:

        feedback.append(
            "🎯 Defina um objetivo profissional para receber "
            "recomendações mais precisas."
        )

    # ==========================================================
    # CONQUISTAS
    # ==========================================================

    feedback.append(
        f"🏅 Conquistas desbloqueadas: {conquistas}"
    )

    # ==========================================================
    # CONTEXTO ACADÊMICO
    # ==========================================================

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

    # ==========================================================
    # PRÓXIMO DESAFIO
    # ==========================================================

    if materia_prioritaria:

        materia = materia_prioritaria["materia"]

        nome_materia = materia["nome"]
        progresso = materia["progresso"]

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

    # ==========================================================
    # PLANO DIÁRIO
    # ==========================================================

    plano_diario = gerar_plano_diario(
        plano,
        materia_prioritaria,
        materias_semestre
    )

    # ==========================================================
    # META SEMANAL
    # ==========================================================

    meta_semanal = gerar_meta_semanal(
        materia_prioritaria,
        materias_semestre
    )

    # ==========================================================
    # MENSAGEM FINAL
    # ==========================================================

    if xp < 100:

        mensagem_final = (
            "💪 Todo profissional começou do zero. "
            "Continue praticando!"
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

    return {
        "feedback": feedback,
        "proximo_desafio": proximo_desafio,
        "meta_semanal": meta_semanal,
        "mensagem_final": mensagem_final,
        "motivo_prioridade": motivo_prioridade,
        "prioridade": prioridade,
        "icone_prioridade": icone_prioridade,
        "plano_diario": plano_diario,
    }


def mostrar_feedback(usuario_id):

    dados = gerar_feedback(usuario_id)

    print("\n╔══════════════════════════════════════════════╗")
    print("║               🤖 AI COACH                   ║")
    print("╚══════════════════════════════════════════════╝")

    print("\nSeu mentor analisou seu desempenho:\n")

    for item in dados["feedback"]:
        print(item)
        print()

    # ==========================================================
    # PRIORIDADE
    # ==========================================================

    if dados["prioridade"]:

        print(
            "══════════════ 🎯 PRIORIDADE DE ESTUDO "
            "══════════════"
        )

        print(
            f"\n{dados['icone_prioridade']} "
            f"PRIORIDADE {dados['prioridade']}"
        )

        print(
            f"📘 {dados['motivo_prioridade']}"
        )

        materia_prioritaria = escolher_materia_prioritaria(
            listar_materias_semestre(usuario_id)
        )

        if materia_prioritaria:

            materia = materia_prioritaria["materia"]

            print(
                f"📚 Matéria: {materia['nome']}"
            )

            print(
                f"📊 Progresso: {materia['progresso']}%"
            )

    # ==========================================================
    # PRÓXIMO DESAFIO
    # ==========================================================

    print("\n🚀 Próximo desafio:")
    print(dados["proximo_desafio"])

    # ==========================================================
    # MOTIVO
    # ==========================================================

    if dados["motivo_prioridade"]:

        print("\n💡 Por que essa matéria?")
        print(dados["motivo_prioridade"])

    # ==========================================================
    # PLANO DIÁRIO
    # ==========================================================

    if dados["plano_diario"]:

        print("\n⏱️ Plano de estudo de hoje:")
        print(dados["plano_diario"])

    # ==========================================================
    # META SEMANAL
    # ==========================================================

    print("\n📅 Meta da semana:")
    print(dados["meta_semanal"])

    # ==========================================================
    # MENSAGEM FINAL
    # ==========================================================

    print("\n" + dados["mensagem_final"])