from services.dashboard_service import obter_dashboard


def test_obter_dashboard(monkeypatch):
    monkeypatch.setattr(
        "services.dashboard_service.total_quizzes",
        lambda usuario_id: 12,
    )

    monkeypatch.setattr(
        "services.dashboard_service.carregar_xp",
        lambda usuario_id: 350,
    )

    monkeypatch.setattr(
        "services.dashboard_service.barra_xp",
        lambda xp: ("███████░░░", 70, 500),
    )

    monkeypatch.setattr(
        "services.dashboard_service.media_quizzes",
        lambda usuario_id: 8.5,
    )

    monkeypatch.setattr(
        "services.dashboard_service.nivel_aluno",
        lambda media: "Avançado",
    )

    monkeypatch.setattr(
        "services.dashboard_service.nivel_xp",
        lambda xp: "🥈 Intermediário",
    )

    monkeypatch.setattr(
        "services.dashboard_service.atualizar_streak",
        lambda usuario_id: 15,
    )

    monkeypatch.setattr(
        "services.dashboard_service.carregar_conquistas",
        lambda usuario_id: ["Primeiro Quiz", "100 XP"],
    )

    dashboard = obter_dashboard(1)

    assert dashboard == {
        "quizzes": 12,
        "xp": 350,
        "barra": "███████░░░",
        "porcentagem": 70,
        "limite": 500,
        "media": 8.5,
        "nivel": "Avançado",
        "rank": "🥈 Intermediário",
        "streak": 15,
        "total_conquistas": 2,
    }