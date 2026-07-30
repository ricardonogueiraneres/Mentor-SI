import sqlite3


BANCO = "mentor.db"


def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():

    conexao = conectar()
    cursor = conexao.cursor()

    # ==========================
    # TABELA USUÁRIO
    # ==========================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            xp INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0,
            ultima_data TEXT DEFAULT '',
            objetivo_profissional TEXT DEFAULT ''
        )
    """)

    try:
        cursor.execute("""
            ALTER TABLE usuario
            ADD COLUMN objetivo_profissional TEXT DEFAULT ''
        """)
    except sqlite3.OperationalError:
        # A coluna já existe
        pass

    # ==========================
    # TABELA QUIZZES
    # ==========================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            materia TEXT NOT NULL,
            pontuacao INTEGER,
            total INTEGER,
            data TEXT,
            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
        ) 
    """)


    # ==========================
    # TABELA PLANOS
    # ==========================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS planos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            objetivo TEXT,
            horas INTEGER,
            data TEXT,
            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
        )
    """)
    
    # ==========================
    # TABELA MISSÕES
    # ==========================


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS missoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            data TEXT,
            missao TEXT,
            concluida INTEGER,
            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conquistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            nome TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuario(id)
       )
    """)


    conexao.commit()
    conexao.close()