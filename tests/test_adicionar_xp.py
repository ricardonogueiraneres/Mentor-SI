from xp import adicionar_xp


def test_adicionar_xp(monkeypatch):
    def falso_carregar_xp(usuario_id):
        return 100

    xp_salvo = {}

    def falso_salvar_xp(usuario_id, xp):
        xp_salvo["usuario_id"] = usuario_id
        xp_salvo["xp"] = xp

    monkeypatch.setattr("xp.carregar_xp", falso_carregar_xp)
    monkeypatch.setattr("xp.salvar_xp", falso_salvar_xp)

    resultado = adicionar_xp(1, 50)

    assert resultado == 150
    assert xp_salvo["usuario_id"] == 1
    assert xp_salvo["xp"] == 150