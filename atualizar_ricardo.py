from banco import conectar
from login import criptografar_senha

conn = conectar()
cursor = conn.cursor()

cursor.execute("""
UPDATE usuario
SET usuario = ?, senha = ?
WHERE nome = ?
""", (
    "ricardo",
    criptografar_senha("1234"),
    "Ricardo"
))

conn.commit()
conn.close()

print("✅ Usuário Ricardo atualizado com sucesso!")