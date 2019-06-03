import socket, psutil
host = socket.gethostname()
porta = 9999
import db
print(db.teste())
# Cria o socket
s = socket.socket()
try:
# Tenta se conectar ao servidor
    s.connect((host, porta))
except Exception as erro:
    print(str(erro))

print('Conexão efetuada com',host)
#Recebe informações disponiveis
msg = s.recv(1024)
print(msg.decode('utf-8'))
while True:
    #Aguarda usuario digitar opção para monitorar
    print('====== \n Seja Bem-Vindo ao BIRD \n======')
    menu = input('Digite a opção que deseja realizar:')
    print(menu)
    if (menu == '1'):
        resposta = input('Digite o usuario para logar-se')
        s.send(resposta.encode('utf-8'))
    s.send(menu.encode('utf-8')) #Envia opção escolhida pelo usuario
    #recebe informações
    info = s.recv(1024)
    print(info.decode())