from services.recomendacao_service import gerar_recomendacao


def test_primeiro_quiz(monkeypatch):
    monkeypatch.setattr(
        "services.recomendacao_service.buscar_xp",
        lambda usuario_id: 0,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_total_quizzes",
        lambda usuario_id: 0,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_streak",
        lambda usuario_id: (0, "")
    )

    assert gerar_recomendacao(1) == (
        "Faça seu primeiro quiz para medir seus conhecimentos."
    )


def test_python_basico(monkeypatch):
    monkeypatch.setattr(
        "services.recomendacao_service.buscar_xp",
        lambda usuario_id: 50,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_total_quizzes",
        lambda usuario_id: 5,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_streak",
        lambda usuario_id: (3, "")
    )

    assert gerar_recomendacao(1) == (
        "Continue estudando Python básico antes de avançar."
    )


def test_streak_zero(monkeypatch):
    monkeypatch.setattr(
        "services.recomendacao_service.buscar_xp",
        lambda usuario_id: 150,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_total_quizzes",
        lambda usuario_id: 10,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_streak",
        lambda usuario_id: (0, "")
    )

    assert gerar_recomendacao(1) == (
        "Estude hoje para iniciar uma nova sequência."
    )


def test_projeto_pratico(monkeypatch):
    monkeypatch.setattr(
        "services.recomendacao_service.buscar_xp",
        lambda usuario_id: 300,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_total_quizzes",
        lambda usuario_id: 20,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_streak",
        lambda usuario_id: (10, "")
    )

    assert gerar_recomendacao(1) == (
        "Excelente evolução! Comece um projeto prático."
    )


def test_recomendacao_padrao(monkeypatch):
    monkeypatch.setattr(
        "services.recomendacao_service.buscar_xp",
        lambda usuario_id: 150,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_total_quizzes",
        lambda usuario_id: 10,
    )

    monkeypatch.setattr(
        "services.recomendacao_service.buscar_streak",
        lambda usuario_id: (5, "")
    )

    assert gerar_recomendacao(1) == (
        "Continue estudando um pouco todos os dias."
    )