import pyautogui
import time

print("********************************")
time.sleep(1)
print("********RAID KILL TOLLS*********")
time.sleep(1)
print("********************************")
pyautogui.PAUSE = 1

time.sleep(1)
print('O Raid Kill Tolls é uma ferramenta que raida várias plataformas e é grátis.')
time.sleep(2.2)
print('por enquanto temos apenas uma versão para pc em breve sai para android.')
time.sleep(2.2)
print('comandos: \n raid ataque \n raid explicações \n raid sair')
time.sleep(1.7)
comando = input('digite o comando que você quer.\n')
if comando == ('raid ataque'):
    time.sleep(1.5)
    print("você entrou no modo ataque de raid kill")
    time.sleep(1)
    loop = int(input("digite o máximo de mensagens que quer(máximo 1000)\n"))
    limite = 1000
    time.sleep(1.5)
    print ('voçê escolheu esse máximo de mensagens\n',loop,)
    time.sleep(1.5)
    print ('seu ataque vai começar em 30 segundos, já deixe a barra de ataque do app que você quer selecionada.')
    time.sleep(30)
    for limite in range(loop):
        pyautogui.hotkey('Ctrl','v')
        pyautogui.press("Enter")
time.sleep(2)
print('sua seção terminou, reinicie o arquivo .py para fazer outro ataque ou outros comandos.')
if comando == ('raid explicações'):
    time.sleep(1.5)
    print("você entrou no modo explicações!")
    time.sleep(2.5)
    print('para que existe esse script ?')
    time.sleep(2.2)
    print('para raidar (encher de mensagem) servidores de trolls e acabar com o servidor deles.')
    time.sleep(2.2)
    print('como fazer os ataques ?')
    time.sleep(2.2)
    print('basta abrir a conversa que quer raidar, clique na barra onde coloca as mensagens \n e basta esperar os 30 segundos.')
time.sleep(2)
print('sua seção terminou, reinicie o arquivo .py para fazer outro ataque ou outros comandos.')
if comando == ('raid sair'):
    print ('você saiu do Raid Kill, reinicie o arquivo .py se quiser fazer ataques ou outros comandos.')