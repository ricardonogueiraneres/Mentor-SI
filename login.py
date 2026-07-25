from database.banco import conectar
import hashlib


def criptografar_senha(senha):
    """Retorna o hash SHA-256 da senha."""
    return hashlib.sha256(senha.encode()).hexdigest()


def usuario_existe(usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM usuario WHERE usuario = ?",
        (usuario,)
    )

    resultado = cursor.fetchone()

    conn.close()

    return resultado is not None


def criar_usuario(nome, usuario, senha):
    """Cria um novo usuário."""

    if usuario_existe(usuario):
        return False

    senha_hash = criptografar_senha(senha)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuario
        (nome, usuario, senha)
        VALUES (?, ?, ?)
    """, (nome, usuario, senha_hash))

    conn.commit()
    conn.close()

    return True


def fazer_login(usuario, senha):
    """Realiza login."""

    senha_hash = criptografar_senha(senha)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM usuario
        WHERE usuario = ?
        AND senha = ?
    """, (usuario, senha_hash))

    dados = cursor.fetchone()

    conn.close()

    return dados