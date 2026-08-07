from database.banco import conectar


def adicionar_colunas_perfil_academico():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("PRAGMA table_info(usuario)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    if "universidade" not in colunas:
        cursor.execute("""
            ALTER TABLE usuario
            ADD COLUMN universidade TEXT DEFAULT ''
        """)

    if "curso" not in colunas:
        cursor.execute("""
            ALTER TABLE usuario
            ADD COLUMN curso TEXT DEFAULT ''
        """)

    if "modalidade" not in colunas:
        cursor.execute("""
            ALTER TABLE usuario
            ADD COLUMN modalidade TEXT DEFAULT ''
        """)

    if "semestre" not in colunas:
        cursor.execute("""
            ALTER TABLE usuario
            ADD COLUMN semestre INTEGER DEFAULT 1
        """)

    if "materias" not in colunas:
        cursor.execute("""
            ALTER TABLE usuario
            ADD COLUMN materias TEXT DEFAULT ''
        """)

    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    adicionar_colunas_login()
    adicionar_colunas_perfil_academico()