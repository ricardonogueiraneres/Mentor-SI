from services.quiz_service import finalizar_quiz


def test_finalizar_quiz_com_bonus(monkeypatch):
    chamadas = []

    def falso_adicionar_xp(usuario_id, valor):
        chamadas.append(("xp", usuario_id, valor))
        return 150 if valor == 100 else 200

    def falso_salvar_quiz(**kwargs):
        chamadas.append(("salvar", kwargs))

    def falso_concluir_missao(nome):
        chamadas.append(("missao", nome))

    def falso_desbloquear(usuario_id, conquista):
        chamadas.append(("conquista", usuario_id, conquista))

    monkeypatch.setattr(
        "services.quiz_service.adicionar_xp",
        falso_adicionar_xp,
    )

    monkeypatch.setattr(
        "services.quiz_service.salvar_quiz",
        falso_salvar_quiz,
    )

    monkeypatch.setattr(
        "services.quiz_service.concluir_missao",
        falso_concluir_missao,
    )

    monkeypatch.setattr(
        "services.quiz_service.desbloquear",
        falso_desbloquear,
    )

    xp, bonus = finalizar_quiz(
        usuario_id=1,
        materia="Python",
        pontos=10,
        total=10,
        xp_quiz=100,
        xp_bonus=50,
    )

    assert xp == 200
    assert bonus is True

    assert ("xp", 1, 100) in chamadas
    assert ("xp", 1, 50) in chamadas
    assert ("missao", "quiz") in chamadas
    assert ("conquista", 1, "Primeiro Quiz") in chamadas

    assert any(item[0] == "salvar" for item in chamadas)