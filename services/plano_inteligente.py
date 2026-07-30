from database.repositorio import (
    buscar_xp,
    buscar_total_quizzes,
    buscar_total_conquistas,
    buscar_objetivo_profissional
)


def gerar_plano_inteligente(usuario_id):

    xp = buscar_xp(usuario_id)
    quizzes = buscar_total_quizzes(usuario_id)
    conquistas = buscar_total_conquistas(usuario_id)
    objetivo = buscar_objetivo_profissional(usuario_id)

    # Definição do foco conforme evolução
    if xp < 100:
        python = 30
        algoritmos = 20
        projeto = 10

        mensagem = (
            "Você ainda está construindo sua base. "
            "Priorize exercícios e lógica de programação."
        )

        meta = "Resolver 10 exercícios de Python."

    elif xp < 300:
        python = 35
        algoritmos = 15
        projeto = 10

        mensagem = (
            "Seu desempenho está evoluindo. "
            "Comece pequenos projetos."
        )

        meta = "Criar um programa usando listas."

    else:
        python = 40
        algoritmos = 15
        projeto = 5

        mensagem = (
            "Você já domina os fundamentos. "
            "Agora é hora de desenvolver projetos completos."
        )

        meta = "Criar um CRUD em Python."

    # Recomendações conforme objetivo profissional
    if objetivo == "Back-end":
        recomendacao = "Estude APIs, SQL, Git e projetos CRUD."

    elif objetivo == "Front-end":
        recomendacao = "Estude HTML, CSS, JavaScript e React."

    elif objetivo == "Inteligência Artificial":
        recomendacao = "Estude Python, Machine Learning, Pandas e IA Generativa."

    elif objetivo == "Ciência de Dados":
        recomendacao = "Estude Python, SQL, Power BI e análise de dados."

    elif objetivo == "Redes":
        recomendacao = "Estude Packet Tracer, IPv4/IPv6, Linux e Cisco."

    elif objetivo == "Banco de Dados":
        recomendacao = "Estude SQL, PostgreSQL, modelagem e otimização."

    elif objetivo == "Segurança da Informação":
        recomendacao = "Estude Linux, redes, OWASP e fundamentos de segurança."

    else:
        recomendacao = (
            "Defina um objetivo profissional para receber recomendações personalizadas."
        )

    return {
        "xp": xp,
        "quizzes": quizzes,
        "conquistas": conquistas,
        "python": python,
        "algoritmos": algoritmos,
        "projeto": projeto,
        "mensagem": mensagem,
        "meta": meta,
        "objetivo": objetivo,
        "recomendacao": recomendacao
    }