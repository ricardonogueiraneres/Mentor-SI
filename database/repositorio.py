from database.banco import conectar


def abrir_cursor():
    conexao = conectar()
    cursor = conexao.cursor()
    return conexao, cursor


def fechar_cursor(conexao):
    conexao.commit()
    conexao.close()


def fechar_conexao(conexao):
    conexao.close()


# ==========================
# USUÁRIO
# ==========================


def carregar_usuario():

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT id, nome, xp, streak
        FROM usuario
        WHERE id = 1
    """)

    usuario = cursor.fetchone()

    fechar_conexao(conexao)

    return usuario

def existe_usuario():

    conexao, cursor = abrir_cursor()

    cursor.execute("SELECT COUNT(*) FROM usuario")

    quantidade = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return quantidade > 0

def buscar_nome(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT nome
        FROM usuario
        WHERE id = ?
    """, (usuario_id,))

    resultado = cursor.fetchone()

    fechar_conexao(conexao)

    if resultado:
        return resultado[0]

    return ""


def salvar_usuario(nome, xp=0, streak=0):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        INSERT INTO usuario(nome, xp, streak)
        VALUES (?, ?, ?)
    """, (nome, xp, streak))

    fechar_cursor(conexao)


def atualizar_nome(nome):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        UPDATE usuario
        SET nome = ?
        WHERE id = 1
    """, (nome,))

    fechar_cursor(conexao)


# ==========================
# XP
# ==========================

def buscar_xp(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT xp
        FROM usuario
        WHERE id = ?
    """, (usuario_id,))

    resultado = cursor.fetchone()

    fechar_conexao(conexao)

    if resultado:
        return resultado[0]

    return 0

def atualizar_xp(usuario_id, xp):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        UPDATE usuario
        SET xp = ?
        WHERE id = ?
    """, (xp, usuario_id))

    fechar_cursor(conexao)

# ==========================
# STREAK
# ==========================

def buscar_streak(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT streak, ultima_data
        FROM usuario
        WHERE id = ?
    """, (usuario_id,))

    resultado = cursor.fetchone()

    fechar_conexao(conexao)

    if resultado:
        return resultado[0], resultado[1]

    return 0, ""

def atualizar_streak_bd(usuario_id, dias, data):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        UPDATE usuario
        SET streak = ?, ultima_data = ?
        WHERE id = ?
    """, (dias, data, usuario_id))

    fechar_cursor(conexao)

# ==========================
# CONQUISTAS
# ==========================

def buscar_conquistas(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT nome
        FROM conquistas
        WHERE usuario_id = ?
    """, (usuario_id,))

    resultado = cursor.fetchall()

    fechar_conexao(conexao)

    return [linha[0] for linha in resultado]

def salvar_conquista(usuario_id, nome):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        INSERT INTO conquistas(usuario_id, nome)
        VALUES (?, ?)
    """, (usuario_id, nome))

    fechar_cursor(conexao)

def buscar_total_conquistas(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM conquistas
        WHERE usuario_id = ?
    """, (usuario_id,))

    total = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return total

# ==========================
# QUIZZES
# ==========================

def salvar_quiz(usuario_id, materia, pontuacao, total, data):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        INSERT INTO quizzes(usuario_id, materia, pontuacao, total, data)
        VALUES (?, ?, ?, ?, ?)
    """, (usuario_id, materia, pontuacao, total, data))

    fechar_cursor(conexao)

def buscar_total_quizzes(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM quizzes
        WHERE usuario_id = ?
    """, (usuario_id,))

    total = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return total

def buscar_total_acertos(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT SUM(pontuacao)
        FROM quizzes
        WHERE usuario_id = ?
    """, (usuario_id,))

    resultado = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return resultado if resultado else 0

def buscar_total_perguntas(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT SUM(total)
        FROM quizzes
        WHERE usuario_id = ?
    """, (usuario_id,))

    resultado = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return resultado if resultado else 0

def buscar_media_quizzes(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT AVG(pontuacao)
        FROM quizzes
        WHERE usuario_id = ?
    """, (usuario_id,))

    resultado = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return resultado if resultado else 0

def buscar_desempenho_por_materia(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT
            materia,
            COUNT(*) AS quizzes,
            SUM(pontuacao) AS acertos,
            SUM(total) AS perguntas,
            AVG(pontuacao) AS media
        FROM quizzes
        WHERE usuario_id = ?
        GROUP BY materia
        ORDER BY media DESC
    """, (usuario_id,))

    resultado = cursor.fetchall()

    fechar_conexao(conexao)

    return resultado

def buscar_historico_quizzes(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT
            data,
            materia,
            pontuacao,
            total
        FROM quizzes
        WHERE usuario_id = ?
        ORDER BY id DESC
    """, (usuario_id,))

    historico = cursor.fetchall()

    fechar_conexao(conexao)

    return historico


# ==========================
# PLANOS DE ESTUDO
# ==========================

def salvar_plano(usuario_id, objetivo, horas, data):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        INSERT INTO planos(usuario_id, objetivo, horas, data)
        VALUES (?, ?, ?, ?)
    """, (usuario_id, objetivo, horas, data))

    fechar_cursor(conexao)

def listar_planos(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT objetivo, horas, data
        FROM planos
        WHERE usuario_id = ?
        ORDER BY data DESC
    """, (usuario_id,))

    planos = cursor.fetchall()

    fechar_cursor(conexao)

    return planos


# ==========================
# MISSÕES
# ==========================

def criar_missoes_do_dia(data):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM missoes
        WHERE usuario_id = 1
        AND data = ?
    """, (data,))

    if cursor.fetchone()[0] == 0:

        for missao in ("ia", "quiz", "plano"):

            cursor.execute("""
                INSERT INTO missoes
                (usuario_id, data, missao, concluida)
                VALUES (?, ?, ?, ?)
            """, (1, data, missao, 0))

    fechar_cursor(conexao)

def buscar_missoes(data):

    criar_missoes_do_dia(data)

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT missao, concluida
        FROM missoes
        WHERE usuario_id = 1
        AND data = ?
    """, (data,))

    resultado = cursor.fetchall()

    fechar_conexao(conexao)

    return {
        nome: bool(concluida)
        for nome, concluida in resultado
    }

def atualizar_missao(data, nome):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        UPDATE missoes
        SET concluida = 1
        WHERE usuario_id = 1
        AND data = ?
        AND missao = ?
    """, (data, nome))

    fechar_cursor(conexao)

def buscar_total_planos(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM planos
        WHERE usuario_id = ?
    """, (usuario_id,))

    total = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return total

def buscar_total_missoes(usuario_id):

    conexao, cursor = abrir_cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM missoes
        WHERE usuario_id = ?
        AND concluida = 1
    """, (usuario_id,))

    total = cursor.fetchone()[0]

    fechar_conexao(conexao)

    return total

