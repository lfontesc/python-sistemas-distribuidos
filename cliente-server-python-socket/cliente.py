import socket, psutil
import ast
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
valor = ast.literal_eval(msg.decode())
print(valor[0])
while True:
    print("\n============= Menu ============= \n 1 - Fazer Login \n 2 - Cadastrar Novo Usuario \n 3 - Listar Usuarios\n 4 - Listar um Usuario Especifico \n 5 - Seguir um Usuario \n 6 - Postar Mensagens \n 7 - Visualizar Mensagens \n 8 - Enviar Menssagem para um Usuario \n 9 - Avaliar Post \n $ - para encerrar a conexão\n================================ \n")
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
        pergunta = input("Deseja marcar alguem [s/n] ?")
        if(pergunta == 's'):
            marcar = input("Digite o nome dos usuarios separado por "','" para marcar: ")
        else:
            marcar = ''
        dic = str([menu,post,marcar])
        s.sendall(dic.encode())
    if (menu == '7'):
        dic = str([menu])
        s.sendall(dic.encode())
    if (menu == '8'):
        mensagem = input("Digite a mensagem: ")
        pergunta = input("Deseja marcar alguem [s/n] ?")
        if(pergunta == 's'):
            marcar = input("Digite o nome dos usuarios separado por "','" para marcar: ")
        else:
            marcar = ''
        dic = str([menu,mensagem,marcar])
        s.sendall(dic.encode())
    if (menu == '9'):
        mensagem = input("Insira o ID da mensagem para avaliar: ")
        resp = input("1 - dar Like\n2 - dar Deslike")
        if(resp == '1'):
            print("usuario deu like")
        else:
            print("usuario deu deslike")

    #s.send(menu.encode()) #Envia opção escolhida pelo usuario
    #recebe informações
    info = s.recv(1024)
    b="'[(,)]"
    if(menu == '3'):
        str1 = info.decode()
        for i in range(0,len(b)):
            str1 = str1.replace(b[i],"")
        str2 = str1.split(" ")
        for i in str2:
            print("Usuario: ",i)
    else:
        print(info.decode())