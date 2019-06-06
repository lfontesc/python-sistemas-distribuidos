import sqlite3
conn = sqlite3.connect('bird.db')
from datetime import datetime


def insertUser(nome,login,senha,email):
    conn = sqlite3.connect('bird.db')
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
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando os dados ao usuário
    cursor.execute("SELECT id FROM usuarios WHERE login = ? and senha = ?", (login,senha))
    dados = cursor.fetchall()
    return dados
    conn.close()

def listarUsuarios():
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("SELECT nome FROM usuarios")
    dados = cursor.fetchall()
    if(len(dados) == 0):
        return 0
    else:
        return dados
    conn.close()

def listarUnicoUsuario(nome):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("SELECT nome,login,email,criado_em FROM usuarios WHERE nome = ? ", (nome,))
    dados = cursor.fetchall()
    print(dados)
    if(len(dados) == 0):
        return 0
    else:
        return dados
    conn.close()

def seguirUsuario(usuario,seguidor):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("""
    INSERT INTO seguidores (idUsuario, idSeguidor)
    VALUES (?,?)
    """, (usuario,seguidor))
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def pesquisarId(login):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("SELECT id FROM usuarios WHERE login = ? ", (login,))
    dados = cursor.fetchall()
    if(len(dados) == 0):
        return 0
    else:
        return dados
    conn.close()

def postarMensagem(idUsuario,texto,marcado):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    criado_em = datetime.today()
    # solicitando lista de usuários
    cursor.execute("""
    INSERT INTO mensagens (idUsuario, texto,mencionados,criado_em)
    VALUES (?,?,?,?)
    """, (idUsuario,texto,marcado,criado_em))
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def darLike(idMensagem):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("""
    UPDATE mensagens SET likes = likes+1 WHERE id = ?
    """, (idMensagem,))
    conn.commit()
    print('Dados alterados com sucesso.')
    conn.close()

def darDeslike(idMensagem):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("""
    UPDATE mensagens SET deslikes = deslikes+1 WHERE id = ?
    """, (idMensagem,))
    conn.commit()
    print('Dados alterados com sucesso.')
    conn.close()


def listarMensagens(idUsuario):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("SELECT p.id,texto,p.criado_em,u.nome,p.likes,p.deslikes FROM mensagens as p JOIN seguidores as s ON s.idSeguidor = p.idUsuario JOIN usuarios as u ON u.id = s.idUsuario WHERE s.idUsuario = ? ORDER BY p.criado_em ", (idUsuario,))
    dados = cursor.fetchall()
    if(len(dados) == 0):
        return 0
    else:
        return dados
    conn.close()

# def enviarMensagem(idEnviado,idRecebido,mensagem):
#     conn = sqlite3.connect('bird.db')
#     cursor = conn.cursor()
#     criado_em = datetime.today()
#     # solicitando lista de usuários
#     cursor.execute("""
#     INSERT INTO mensagem (idUsuarioEnviado, idUsuarioRecebido, mensagem,criado_em)
#     VALUES (?,?,?,?)
#     """, (idEnviado,idRecebido, mensagem,criado_em))
#     conn.commit()
#     print('Dados inseridos com sucesso.')
#     conn.close()

def estaSeguindo(idSeguidor,idUsuario):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("SELECT * FROM seguidores WHERE idSeguidor = ? and idUsuario = ? ", (idSeguidor,idUsuario,))
    dados = cursor.fetchall()
    if(len(dados) == 0):
        return False
    else:
        return True
    conn.close()

def quantoslikes(idMensagem):
    conn = sqlite3.connect('bird.db')
    cursor = conn.cursor()
    # solicitando lista de usuários
    cursor.execute("SELECT likes FROM mensagens WHERE id = ?", (idMensagem,))
    dados = cursor.fetchall()
    return dados
    conn.close()

#print(verificarLogin("fontes","fontes001"))
#insertUser("cartaxo","cartaxo1","cartaxo001","cartaxo@gmail.com")
#listarUsuarios()
#listarUnicoUsuario("cartaxo")
#seguirUsuario(1,20)
#print(pesquisarId("fontes"))
#postar(1,"isso é so um teste viu, tenha calma xD xD")
#print(listarPosts(1))
#enviarMensagem(100,100,"testando o envio de mensagem")
#print(estaSeguindo(20,1))
#postarMensagem(1,"dkslkdsldskll","fontes,lucas")
#darLike(7)
#darDeslike(7)
#print(pesquisarId("samu"))

#dado = quantoslikes(11)
#print(dado[0][0])