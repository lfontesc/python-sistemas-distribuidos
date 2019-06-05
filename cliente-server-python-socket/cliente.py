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
print("\n")
print(msg.decode())
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
    if (menu == '3'):
        dic = str([menu])
        s.sendall(dic.encode())
    if (menu == '4'):
        nome = input("Digite o nome do usuario: ")
        dic = str([menu,nome])
        s.sendall(dic.encode())
    if (menu == '5'):
        login = input("Digite o username do usuario: ")
        dic = str([menu,login])
        s.sendall(dic.encode())
    if (menu == '6'):
        post = input("Digite o texto do post: ")
        dic = str([menu,post])
        s.sendall(dic.encode())
    if (menu == '7'):
        dic = str([menu])
        s.sendall(dic.encode())
    #s.send(menu.encode()) #Envia opção escolhida pelo usuario
    #recebe informações
    info = s.recv(1024)
    print(info.decode())