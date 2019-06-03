# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('bird.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE usuarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        login TEXT NOT NULL,
        senha VARCHAR(20) NOT NULL,
        email TEXT NOT NULL,
        criado_em DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()