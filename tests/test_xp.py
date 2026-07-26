from xp import nivel_xp
from xp import barra_xp


def test_nivel_iniciante():
    assert nivel_xp(0) == "🌱 Iniciante"


def test_nivel_aprendiz():
    assert nivel_xp(100) == "📘 Aprendiz"


def test_nivel_intermediario():
    assert nivel_xp(250) == "🥈 Intermediário"


def test_nivel_avancado():
    assert nivel_xp(500) == "🥇 Avançado"


def test_nivel_especialista():
    assert nivel_xp(1000) == "🏆 Especialista"


def test_nivel_mestre():
    assert nivel_xp(2000) == "👑 Mestre Mentor"


def test_barra_iniciante():
    barra, porcentagem, limite = barra_xp(50)

    assert barra == "█████░░░░░"
    assert porcentagem == 50
    assert limite == 100


def test_barra_aprendiz():
    barra, porcentagem, limite = barra_xp(125)

    assert barra == "█████░░░░░"
    assert porcentagem == 50
    assert limite == 250


def test_barra_intermediario():
    barra, porcentagem, limite = barra_xp(250)

    assert barra == "█████░░░░░"
    assert porcentagem == 50
    assert limite == 500


def test_barra_avancado():
    barra, porcentagem, limite = barra_xp(500)

    assert barra == "█████░░░░░"
    assert porcentagem == 50
    assert limite == 1000


def test_barra_especialista():
    barra, porcentagem, limite = barra_xp(1000)

    assert barra == "█████░░░░░"
    assert porcentagem == 50
    assert limite == 2000


def test_barra_maxima():
    barra, porcentagem, limite = barra_xp(3000)

    assert barra == "██████████"
    assert porcentagem == 100
    assert limite == 2000