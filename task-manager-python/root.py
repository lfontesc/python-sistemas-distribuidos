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
def listaProcessosUsuario(user):
    pids = psutil.pids()
    print('-' * 45)
    for i in pids:
        if(user == psutil.Process(i).username()):
            #print('PID NAME USERNAME PRIO.')
            infoProcesso(i)

# informações de um processo
def infoProcesso(pid):
    #logica para pegar a hora do processo
    horap = datetime.fromtimestamp(psutil.Process(pid).create_time())
    horaa = datetime.now()
    #o time recebe a hora atual menos a hora que o processo iniciou, levando a quaunto tempo o processo está executando
    time = str(horaa - horap)
    #mostrando a info do processo
    print("PID:",psutil.Process(pid).pid,"NAME:",psutil.Process(pid).name(),"USER:",psutil.Process(pid).username(),"NICE:",psutil.Process(pid).nice(),"STATUS",psutil.Process(pid).status(),"TIME",time[0:7])
    print ('-' * 45)

# bloquear um processo
def bloquearProcesso(pid):
    #verifica se o processo ja esta bloqueado, se não estiver ele bloqueia 
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

#executar processo
def executarProcesso(path):
    #iniciando um sub processo chamando ele pelo comando em um terminal novo
    subprocess.call(['xfce4-terminal', '-e', '%s'  %(path,)])
    #subprocess.Popen('xterm -e "%s"' % command)
    print('Processo criado com sucesso!')

#reiniciar processo
def reiniciarProcesso(pid):
    #salva o proceso, finaliza e depois executa denovo
    processo = psutil.Process(pid).exe()
    finalizarProcesso(pid)
    subprocess.call(['xfce4-terminal', '-e', '%s' %(processo,)])
   # subprocess.Popen(processo)
    print('Proceso reiniciado com sucesso.') 

#finalizar processo
def finalizarProcesso(pid):
    #.terminate() para terminar o processo
    psutil.Process(pid).terminate()
    print('Processo foi finalizado com sucesso.')

def baixarPrioridade(pid):
    processo = psutil.Process(pid)
    #alterando o nice de 1 em 1
    nice = processo.nice()
    nice = nice + 1
    processo.nice(nice)
    print('Prioridade do processo foi baixada')

def aumentarPrioridade(pid):
    processo = psutil.Process(pid)
    nice = processo.nice()
    nice = nice - 1
    processo.nice(nice)
    print('Prioridade do processo foi aumentada')


##função principal onde vai rodar o menu
if __name__=='__main__':
    while(1):
        #menu
        print("======== Task Manager V0.8 ========")
        print('1 - Listar processos de um usuario.')
        print('2 - Informacoes de um processo.')
        print('3 - Alterar Estado de um processo.')
        print('4 - Alterar Prioridade de um processo.')
        print('5 - Sair')
        print("===================================")
        menu = int(input("root@root-$ "))
        if(menu == 1):
            user = input('Digite o usuario para buscar os seus processos: ')
            listaProcessosUsuario(user)      
        elif(menu == 2):
            print('Informe o PID do processo desejado: ')
            pid = int(input())
            infoProcesso(pid)
        elif(menu == 3):
            print('Selecione um estado:')
            print('1 - Bloquear processo.')
            print('2 - Continuar processo.')
            print('3 - Executar processo.')
            print('4 - Reiniciar processo.')
            print('5 - Finalizar processo.')
            estado = int(input())
            if (estado == 1):
                pid = int(input('Digite o PID do processo: '))
                bloquearProcesso(pid)
            elif (estado == 2):
                pid = int(input('Digite o PID do processo: '))
                continuarProcesso(pid)
            elif (estado == 3):
                path = (input('Digite o PATH do processo: '))
                executarProcesso(path)
            elif (estado == 4):
                pid = int(input('Digite o PID do processo: '))
                reiniciarProcesso(pid)
            elif (estado == 5):
                pid = int(input('Digite o PID do processo: '))
                finalizarProcesso(pid)
            else:
                print('Selecione uma opcao do MENU')
        elif(menu == 4):
            print('Selecione uma opcao:')
            print('1 - Baixar prioridade.')
            print('2 - Aumentar prioridade.')
            mn3 = int(input())
            if (mn3 == 1):
                pid = int(input('Digite o PID do processo para baixar prioridade:'))
                baixarPrioridade(pid)
            elif (mn3 == 2):
                pid = int(input('Digite o PID do processo para aumentar prioridade:'))
                aumentarPrioridade(pid)
            else:
                print('Selecione uma opcao do MENU:')
        elif(menu == 5):
                exit()
        else:
            print('Selecione uma Opção que está apenas no MENU')

main()