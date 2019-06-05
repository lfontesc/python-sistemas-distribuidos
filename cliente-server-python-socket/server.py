import ast
import socket, psutil
import database

# Cria o socket
socket_servidor = socket.socket()
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))
# dic = str([menu,mensagem,marcar])
#         s.sendall(dic.encode())
info5 = ("\n================================== \n Seja Bem-Vindo ao BIRD \n==================================\nVocê não está logado, por favor digite 1 para se logar.\n")
#socket_cliente.send(info5.encode('utf-8')) # Envia mensagem
dic = str([info5])
socket_cliente.sendall(dic.encode())
logado = False

#terminou = False
while True:
    #info = ("\n============= Menu ============= \n 1 - Fazer Login \n 2 - Cadastrar Novo Usuario \n 3 - Listar Usuarios\n 4 - Listar um Usuario Especifico \n 5 - Seguir um Usuario \n 6 - Postar Mensagens \n 7 - Visualizar Mensagens \n 8 - Enviar Menssagem para um Usuario \n 9 - Avaliar Post \n $ - para encerrar a conexão\n ================================ \n")
    #socket_cliente.send(info.encode('utf-8')) # Envia resposta
    msg = socket_cliente.recv(1024)
    valor = ast.literal_eval(msg.decode())
    if '$' == msg.decode('utf-8'): #Termino do cliente
        info = ('Conexão encerrada')
        socket_cliente.send(info.encode('utf-8')) # Envia mensagem
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    if '1' == valor[0]:
        info1 = ('O usuario solicitou fazer o login no BIRD')
        info2 = database.verificarLogin(valor[1],valor[2])
        if(len(info2) == 0):
            logado = False
            print("Login ou senha errada tente novamente")
            info = ("Tente novamente")
            socket_cliente.send(info.encode('utf-8')) # Envia resposta
        else:
            logado = True
            idUsuario = info2[0]
            info = ('~ Você está logado no BIRD ~\n')
            socket_cliente.send(info.encode('utf-8'))
            print("Login Efetuado com Sucesso")
        #socket_cliente.send(info1.encode('utf-8')) # Envia mensagem
        #print(info1)
        #login = socket_cliente.recv(1024)
        #senha = socket_cliente.recv(1024)
        #print(type(login))
        #print(senha)
        
    if '2' == valor[0]:
        info2 = database.insertUser(valor[1],valor[2],valor[3],valor[4])
        info = ("\n Dados cadastrados com sucesso\n")
        socket_cliente.send(info.encode('utf-8')) # Envia mensagem

    if '3' == valor[0]:
        info3 = str(database.listarUsuarios())
        socket_cliente.send(info3.encode()) # Envia mensagem
        
    if '4' == valor[0]:
        info3 = str(database.listarUnicoUsuario(valor[1]))
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        #print(info3)
        
    if '5' == valor[0]:
        resultado = database.pesquisarId(valor[1])
        if(logado == False):
            info = ("Você não está logado por favor faça o login")
            socket_cliente.send(info.encode('utf-8')) # Envia mensagem
        else: 
            info3 = database.seguirUsuario(idUsuario[0],resultado[0][0])
            info = ("Agora você está seguindo esse usuario")
            socket_cliente.send(info.encode('utf-8')) # Envia mensagem
        #print(info3)
    
    if '6' == valor[0]:
        db = database.postarMensagem(idUsuario[0],valor[1],valor[2])
        info = ("Post efetuado com sucesso")
        socket_cliente.send(info.encode())

    if '7' == valor[0]:
        db = str(database.listarMensagens(idUsuario[0]))
        socket_cliente.send(db.encode())

    if '8' == valor[0]:
        resultado = database.pesquisarId(valor[1])
        estaSeguindo = database.estaSeguindo(idUsuario[0],resultado[0][0])
        if(estaSeguindo):
            db = database.enviarMensagem(idUsuario[0],resultado[0][0],valor[1])
            info = ("Mensagem enviada com sucesso")
            socket_cliente.send(info.encode())
        else:
            info = ("Você não pode enviar uma mensagem, pois não está seguindo esse usuario")
            socket_cliente.send(info.encode())
    else:
        pass