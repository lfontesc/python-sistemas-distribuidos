import socket, psutil
host = socket.gethostname()
porta = 9999

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
# Tenta se conectar ao servidor
    s.connect((host, porta))
except Exception as erro:
    print(str(erro))

print('Conexão efetuada com',host)
#Recebe informações disponiveis
msg = s.recv(1024)
print(msg)
while True:
    #Aguarda usuario digitar opção para monitorar
    #print('====== \n Seja Bem-Vindo ao BIRD \n======')
    menu = input('Digite a opção que deseja realizar:')

    if (menu == '1'):
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        dic = str([menu,login,senha])
        s.sendall(dic.encode())
    if (menu == '2'):
        nome = input("Digite o nome: ")
        login = input("Digite a login: ")
        senha = input("Digite o senha: ")
        email = input("Digite a email: ")
        dic = str([menu,login,nome,senha,email])
        s.sendall(dic.encode())
    #s.send(menu.encode()) #Envia opção escolhida pelo usuario
    #recebe informações
    info = s.recv(1024)
    print(info.decode())