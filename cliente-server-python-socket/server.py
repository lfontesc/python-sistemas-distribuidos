import ast
import socket, psutil
import database
#print(database.verificarLogin("fontes","fontes001"))

def mostra_uso_ram():
    mem = psutil.virtual_memory()
    text = '\nMemoria Total: {}'.format(mem.total/(1024*1024*1024))
    text += '\nMemoria Usada: {}'.format(mem.used/(1024*1024*1024))
    return text

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


#terminou = False
while True:
    logado = False
    info = ("============= Menu ============= \n 1 - Fazer Login \n 2 - Cadastrar Novo Usuario \n 3 - Listar Usuarios\n 4 - Listar um Usuario Especifico \n 5 - Seguir um Usuario \n 6 - Visualizar Posts \n 7 - Enviar Menssagem para um Usuario \n 8 - Avaliar Post \n Pressione $ para encerrar a conexão")
    socket_cliente.send(info.encode('utf-8')) # Envia resposta
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
        if(info2):
            logado = True
            info = ('=======================\n Você está logado no BIRD\n=======================')
            socket_cliente.send(info.encode('utf-8'))
            print("Login Efetuado com Sucesso")
        else:
            logado = False
            print("Login ou senha errada tente novamente")
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

    if '3' == msg.decode('UTF-8'):
        info3 = ('Usuario solicitou Informações sobre arquivos e diretorios')
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        print(info3)
        
    if '4' == msg.decode('UTF-8'):
        info3 = ('Usuario solicitou Informações sobre processos ativos')
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        print(info3)
        
    if '5' == msg.decode('UTF-8'):
        info3 = database.verificarLogin("fontes","fontes001")
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        print(info3)
        
    else:
        pass