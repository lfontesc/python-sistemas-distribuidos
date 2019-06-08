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
# transforma a mensagem em uma lista
valor = ast.literal_eval(msg.decode())
print(valor[0])
while True:
    # imprime o menu de ações que um usuario pode fazer no sistema
    print("\n============= Menu ============= \n 1 - Fazer Login \n 2 - Cadastrar Novo Usuario \n 3 - Listar Usuarios\n 4 - Listar um Usuario Especifico \n 5 - Seguir um Usuario \n 6 - Postar Mensagens \n 7 - Visualizar Mensagens \n 8 - Enviar Menssagem para um Usuario \n 9 - Avaliar Post \n 10 - Quantos Likes tem ? \n $ - para encerrar a conexão\n================================ \n")
    #Aguarda usuario digitar opção para monitorar
    #print('====== \n Seja Bem-Vindo ao BIRD \n======')
    menu = input('Digite a opção que deseja realizar:')

    if (menu == '1'): # manda login e senha para fazer o login
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")
        # é enviado um dicionado em forma de String contendo a operação, login e senha
        dic = str([menu,login,senha])
        s.sendall(dic.encode())
    if (menu == '2'): # opção para cadastrar novo usuario
        nome = input("Digite o nome: ")
        login = input("Digite a login: ")
        senha = input("Digite o senha: ")
        email = input("Digite a email: ")
        dic = str([menu,login,nome,senha,email])
        s.sendall(dic.encode())
    if (menu == '3'): # opção para listar todos os usuarios 
        dic = str([menu])
        s.sendall(dic.encode())
    if (menu == '4'): # manda a opção de listar um usuario especifico 
        nome = input("Digite o nome do usuario: ")
        dic = str([menu,nome])
        s.sendall(dic.encode())
    if (menu == '5'): # seguir um usuario
        login = input("Digite o username do usuario: ")
        dic = str([menu,login])
        s.sendall(dic.encode())
    if (menu == '6'): # postar uma mensagem 
        post = input("Digite o texto do post: ")
        pergunta = input("Deseja marcar alguem [s/n] ?") # pergunta se deseja marcar alguem no post
        if(pergunta == 's'):
            marcar = input("Digite o nome dos usuarios separado por "','" para marcar: ")
        else:
            marcar = ''
        dic = str([menu,post,marcar])
        s.sendall(dic.encode())
    if (menu == '7'):  # manda operação para visualizar todas as mensagens de quem esta seguindo
        dic = str([menu])
        s.sendall(dic.encode())
    if (menu == '8'): # opção desativada pois essa função estava na opção 6
        mensagem = input("Digite a mensagem: ")
        pergunta = input("Deseja marcar alguem [s/n] ?")
        if(pergunta == 's'):
            marcar = input("Digite o nome dos usuarios separado por "','" para marcar: ")
        else:
            marcar = ''
        dic = str([menu,mensagem,marcar])
        s.sendall(dic.encode())
    if (menu == '9'): # avaliar post, e pergunta se quer avaliar positivamente ou negativamente
        mensagem = input("Insira o ID da mensagem para avaliar: ")
        resp = input("1 - dar Like\n2 - dar Deslike")
        dic = str([menu,mensagem,resp])
        s.sendall(dic.encode())
    if (menu == '10'): #visualizar quantidade de likes de um post 
        mensagem = input("Insira o ID da mensagem: ")
        dic = str([menu,mensagem])
        s.sendall(dic.encode())
    else:
        pass
    #s.send(menu.encode()) #Envia opção escolhida pelo usuario
    #recebe informações 
    # a partir daqui o servidor vai mandar repostas de acordo com a opção que mandamos para ele
    info = s.recv(1024)
    b="'[(,)]" # string para poder tratar a resposta do servidor retirando esses caracteres

    if(menu == '3'):
        print("\nLista de Usuarios: ")
        str1 = info.decode() # tira todos os caracteres indesejados da string da lista de usuario
        for i in range(0,len(b)):
            str1 = str1.replace(b[i],"")
        str2 = str1.split(" ")
        for i in str2:
            print("Usuario: ",i)
    if(menu == '4'): 
        msg = info.decode()
        if(msg == '0'): # se o usuario que a pessoa digitou para ver a mensagem não existir esse erro é tratado
            print("Usuario Não existe, tente novamente.")
        else:
            for i in range(0,len(b)): # retira todos os caracteres indesejados
                msg = msg.replace(b[i],"")
            str2 = msg.split(" ")
            print("nome: ",str2[0]) # imprime todas as informaçoes dos usuarios que foi transformada em string de lista na linha acima
            print("username: ",str2[1])
            print("email: ",str2[2])
            print("Usuario desde: ",str2[3])
    if(menu == '10'): #tira os caracteres indesejados
        msg = info.decode()
        b="[,()]"
        for i in range(0,len(b)):
            msg = msg.replace(b[i],"")
        print("Essa postagem tem: ", msg,"avaliações")
    if(menu == '7'): 
        #msg = info.decode()
        if(msg == '0'): # verifica se não tem nenhuma mensagem
            print("Nenhuma mensagem ainda. ")
        else:
            vartipo = pickle.loads(info) # reverte a serialização da lista em bytes que foi mandada do servidor
            print("\n----------- Lista de Mensagens -----------\n")
            for i in vartipo:
                print("************ Mensagem ************")
                print("ID: ",i[0])
                print("Username: ", i[3])
                print("Mensagem: ", i[1])
                print("enviada em: ",i[2])
                print("**********************************\n")
            print("--------------------------------------------\n")
    if(menu == '1'): # a partir daqui foi só gambiarra para funcionar o resto da impressão dos menus
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