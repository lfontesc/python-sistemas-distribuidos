import sqlite3
conn = sqlite3.connect('bird.db')
from datetime import datetime


def insertUser(nome,login,senha,email):
    cursor = conn.cursor()
    # solicitando os dados ao usuário
    p_criado_em = datetime.today()
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO usuarios (nome, login, senha, email, criado_em)
    VALUES (?,?,?,?,?)
    """, (nome,login,senha,email, p_criado_em))
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def verificarLogin(login,senha):
    cursor = conn.cursor()
    # solicitando os dados ao usuário
    cursor.execute("SELECT login,senha FROM usuarios WHERE login = ? and senha = ?", (login,senha))
    dados = cursor.fetchall()

    if(len(dados) == 0):
        return False
    else:
        return True
    conn.close()

#print(verificarLogin("fontes","fontes001"))
#insertUser("cartaxo","cartaxo1","cartaxo001","cartaxo@gmail.com")