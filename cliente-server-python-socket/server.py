import socket, psutil

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
    info = ("\n 1 - Uso de Processamento \n 2 - Memoria \n 3- Arquivos e Diretórios\n 4 -Processos Ativos \n 5- Redes \n Pressione $ para encerrar a conexão")
    socket_cliente.send(info.encode('utf-8')) # Envia resposta
    msg = socket_cliente.recv(1024)
    print(msg)
    if '$' == msg.decode('utf-8'): #Termino do cliente
        info = ('Conexão encerrada')
        socket_cliente.send(info.encode('utf-8')) # Envia mensagem
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    if '1' == msg.decode('utf-8'):
        info1 =('Usuario solicitou Informações de uso de processamento')
        socket_cliente.send(info1.encode('utf-8')) # Envia mensagem
        print(info1)
        break
    if '2' == msg.decode('UTF-8'):
        info2 = ('Usuario solicitou Informações sobre Memoria')
        mem = mostra_uso_ram()
        socket_cliente.send(mem.encode('utf-8')) # Envia mensagem
        print(info2, mem)
        break
    if '3' == msg.decode('UTF-8'):
        info3 = ('Usuario solicitou Informações sobre arquivos e diretorios')
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        print(info3)
        break
    if '4' == msg.decode('UTF-8'):
        info3 = ('Usuario solicitou Informações sobre processos ativos')
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        print(info3)
        break
    if '5' == msg.decode('UTF-8'):
        info3 = ('Usuario solicitou Informações sobre Rede')
        socket_cliente.send(info3.encode('utf-8')) # Envia mensagem
        print(info3)
        break
    else:
        dif =('O usuário Digitou opções invalidas.')
        socket_cliente.send(dif.encode('utf-8')) # Envia resposta
        socket_cliente.send(info.encode('utf-8')) # Envia resposta
        print('O usuário Digitou opções invalidas.')
        break