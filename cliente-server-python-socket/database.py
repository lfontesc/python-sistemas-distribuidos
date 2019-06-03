import sqlite3
conn = sqlite3.connect('bird.db')


def insertUser():
    cursor = conn.cursor()
    # solicitando os dados ao usuário
    p_nome = input('Nome: ')
    p_login = input('Login: ')
    p_senha = input('Senha: ')
    p_email = input('Email: ')
    p_criado_em = input('Criado em (yyyy-mm-dd): ')
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO usuarios (nome, login, senha, email, criado_em)
    VALUES (?,?,?,?,?)
    """, (p_nome, p_login, p_senha, p_email, p_criado_em))
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def verificarLogin(login,senha):
    cursor = conn.cursor()
    # solicitando os dados ao usuário
    cursor.execute("SELECT login,senha FROM usuarios WHERE login = ? and senha = ?", (login,senha))
    if(cursor == 0):
        return False
    else:
        return True
    conn.close()

#print(verificarLogin("fontes","fontes001"))