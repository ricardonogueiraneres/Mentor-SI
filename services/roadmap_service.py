from database.repositorio import buscar_objetivo_profissional
from estatisticas import total_quizzes
from xp import carregar_xp


def obter_status_etapa(xp: int, indice: int) -> str:
    """
    Retorna o status da etapa baseado no XP do aluno.
    """

    limite = (indice + 1) * 150

    if xp >= limite:
        return "✅"
    elif xp >= limite - 75:
        return "🟡"
    else:
        return "⬜"


def gerar_roadmap(usuario_id: int) -> dict:
    """
    Gera um roadmap personalizado para o aluno.
    """

    objetivo = buscar_objetivo_profissional(usuario_id)
    xp = carregar_xp(usuario_id)
    quizzes = total_quizzes(usuario_id)

    # Define as etapas conforme o objetivo
    if objetivo == "Back-end":
        etapas = [
            "Aprender Python",
            "Aprender Git e GitHub",
            "Criar CRUD",
            "Consumir APIs",
            "Criar API com Flask/FastAPI",
            "Banco de Dados SQL",
            "Projeto completo",
            "Portfólio",
            "Currículo",
            "Enviar currículo",
        ]

    elif objetivo == "Front-end":
        etapas = [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "GitHub",
            "Projeto Responsivo",
            "Portfólio",
            "Currículo",
            "Enviar currículo",
        ]

    elif objetivo == "Inteligência Artificial":
        etapas = [
            "Python",
            "Git",
            "APIs",
            "Gemini/OpenAI",
            "Machine Learning",
            "Projeto de IA",
            "Portfólio",
            "Currículo",
            "Primeira vaga",
        ]

    elif objetivo == "Ciência de Dados":
        etapas = [
            "Python",
            "Pandas",
            "NumPy",
            "SQL",
            "Power BI",
            "Machine Learning",
            "Portfólio",
            "Currículo",
            "Primeira vaga",
        ]

    else:
        etapas = [
            "Definir objetivo profissional"
        ]

    # Calcula o progresso geral
    progresso = min(100, int((xp / 1500) * 100))

    # Adiciona os ícones de status
    etapas_formatadas = []

    for indice, etapa in enumerate(etapas):
        status = obter_status_etapa(xp, indice)
        etapas_formatadas.append(f"{status} {etapa}")

    return {
        "objetivo": objetivo,
        "progresso": progresso,
        "xp": xp,
        "quizzes": quizzes,
        "etapas": etapas_formatadas,
    }
