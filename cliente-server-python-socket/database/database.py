import sqlite3
conn = sqlite3.connect('bird.db')
cursor = conn.cursor()

def insertUser(nome,login,senha,email,criado_em):
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