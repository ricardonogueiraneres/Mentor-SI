from banco import conectar


def adicionar_colunas_login():
    conn = conectar()
    cursor = conn.cursor()

    # Descobre as colunas existentes
    cursor.execute("PRAGMA table_info(usuario)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    if "usuario" not in colunas:
        cursor.execute(
            "ALTER TABLE usuario ADD COLUMN usuario TEXT"
        )
        print("✅ Coluna 'usuario' adicionada.")

    if "senha" not in colunas:
        cursor.execute(
            "ALTER TABLE usuario ADD COLUMN senha TEXT"
        )
        print("✅ Coluna 'senha' adicionada.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    adicionar_colunas_login()