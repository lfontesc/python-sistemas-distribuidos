import socket, psutil
import ast
import pickle

#informações sobre o socket 
host = socket.gethostname()
porta = 9999

## Lucas Fontes Cartaxo
## Francisco Maycon Lima Silva
## Elias Sampaio dos Santos

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
    print("\n============= Menu ============= \n 1 - Fazer Login \n 2 - Cadastrar Novo Usuario \n 3 - Listar Usuarios\n 4 - Listar um Usuario Especifico \n 5 - Seguir um Usuario \n 6 - Postar Mensagens \n 7 - Visualizar Mensagens \n 8 - Enviar Menssagem para um Usuario \n 9 - Avaliar Post \n 10 - Quantos Likes tem ? \n $ - para encerrar a conexão\n================================ \n")
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
        dic = str([menu,mensagem,resp])
        s.sendall(dic.encode())
    if (menu == '10'):
        mensagem = input("Insira o ID da mensagem: ")
        dic = str([menu,mensagem])
        s.sendall(dic.encode())
    else:
        pass
    #s.send(menu.encode()) #Envia opção escolhida pelo usuario
    #recebe informações
    info = s.recv(1024)
    b="'[(,)]"

    if(menu == '3'):
        print("\nLista de Usuarios: ")
        str1 = info.decode()
        for i in range(0,len(b)):
            str1 = str1.replace(b[i],"")
        str2 = str1.split(" ")
        for i in str2:
            print("Usuario: ",i)
    if(menu == '4'):
        msg = info.decode()
        if(msg == '0'):
            print("Usuario Não existe, tente novamente.")
        else:
            for i in range(0,len(b)):
                msg = msg.replace(b[i],"")
            str2 = msg.split(" ")
            print("nome: ",str2[0])
            print("username: ",str2[1])
            print("email: ",str2[2])
            print("Usuario desde: ",str2[3])
    if(menu == '10'):
        msg = info.decode()
        b="[,()]"
        for i in range(0,len(b)):
            msg = msg.replace(b[i],"")
        print("Essa postagem tem: ", msg,"avaliações")
    if(menu == '7'):
        #msg = info.decode()
        if(msg == '0'):
            print("Nenhuma mensagem ainda. ")
        else:
            vartipo = pickle.
            (info)
            print("\n----------- Lista de Mensagens -----------\n")
            for i in vartipo:
                print("************ Mensagem ************")
                print("ID: ",i[0])
                print("Username: ", i[3])
                print("Mensagem: ", i[1])
                print("enviada em: ",i[2])
                print("**********************************\n")
            print("--------------------------------------------\n")
    if(menu == '1'):
        msg = info.decode()
        print(info.decode())
    if(menu == '2'):
        msg = info.decode()
        print(info.decode())        
    if(menu == '5'):
        msg = info.decode()
        print(info.decode())
    if(menu == '6'):
        msg = info.decode()
        print(info.decode())
    if(menu == '8'):
        msg = info.decode()
        print(info.decode())

    ##3471012