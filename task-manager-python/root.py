#Trabalho Sistemas Distribuidos N1
#Lucas, Maycon e Elias
# todo list = a> listar processos de um usuario
# b> permitir consultar infos de um processo com "pid, nice, user, time, status"
# c> permitir alterar estado de um processo com "bloquear,continuar,executar, reiniciar, finalizar"
# d> trocar prioridade de execução antes de ser executado ou em execução

import os
import psutil
import subprocess
from datetime import timedelta,datetime

# listar processos de um usuario
def listaProcessosUsuario():
    usuario = 'fontes'
    pids = psutil.pids()
    print('-' * 45)
    for i in pids:
        if(usuario == psutil.Process(i).username()):
            #print('PID NAME USERNAME PRIO.')
            infoProcesso(i)
# informações de um processo
def infoProcesso(pid):
    horap = datetime.fromtimestamp(psutil.Process(pid).create_time())
    horaa = datetime.now()
    time = str(horaa - horap)
    print(psutil.Process(pid).pid,psutil.Process(pid).name(), psutil.Process(pid).username(),psutil.Process(pid).nice(),psutil.Process(pid).status(),time[0:7])
    print ('-' * 45)

# bloquear um processo
def bloquearProcesso(pid):
    if(psutil.Process(pid).status() != 'stopped'):
        psutil.Process(pid).suspend()
        print('O processo foi bloqueado.')
    else:
        print('O processo já esta bloqueado')

#continuar processo
def continuarProcesso(pid):
    if psutil.Process(pid).status() == 'stopped':
        psutil.Process(pid).resume()
        print('Processo continuado com sucesso.')
    else:
        print('O processo nao encontra-se bloqueado.')

##função principal onde vai rodar o menu
if __name__=='__main__':
    while(1):
        print("======== Task Manager V0.2 ========")
        print('1 - Listar processos de um usuario.')
        print('2 - Informacoes de um processo.')
        print('3 - Alterar Estado de um processo.')
        print('4 - Alterar Prioridade de um processo.')
        mn = int(input("root: "))
        if(mn == 1):
            listaProcessosUsuario()      
        elif(mn == 2):
            print('Informe o PID do processo desejado')
            pid = int(input())
            infoProcesso(pid)
        elif(mn == 3):
            print('Selecione um estado:')
            print('1 - Bloquear processo.')
            print('2 - Continuar processo.')
            print('3 - Executar processo.')
            print('4 - Reiniciar processo.')
            print('5 - Finalizar processo.')
            estado = int(input())
            if (estado == 1):
                pid = int(input('Digite o PID do processo:'))
                bloquearProcesso(pid)
            elif (estado == 2):
                pid = int(input('Digite o PID do processo:'))
                continuarProcesso(pid)
            elif (estado == 3):
                pid = (input('Digite o PATH do processo:'))
               
            elif (estado == 4):
                pid = int(input('Digite o PID do processo:'))
               
            elif (estado == 5):
                pid = int(input('Digite o PID do processo:'))
            else:
                print('Selecione uma opcao do MENU')
        elif(mn == 4):
            print('Selecione uma opcao:')
            print('1 - Baixar prioridade.')
            print('2 - Aumentar prioridade.')
            mn3 = int(input())
            if (mn3 == 1):
                pid = int(input('Digite o PID do processo desejado:'))
      
            elif (mn3 == 2):
                pid = int(input('Digite o PID do processo desejado:'))
               
            else:
                print('Selecione uma opcao do MENU:')
        else:
            print('Selecione uma Opção que está apenas no MENU')

main()