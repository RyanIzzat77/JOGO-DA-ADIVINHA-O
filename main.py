import msvcrt
import os
from random import randint

#função que verifica se o usuário apertou ENTER
def press_enter_to_continue():
    print("Pressione ENTER para iniciar...")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':  # Verifica se a tecla pressionada é Enter
                break

press_enter_to_continue()
print("Continuando...")
print('-'*30)
print('SORTEAMOS UM NÚMERO ENTRE 0 E 100')
print('-'*30)

while True:
    numero_sorteado = randint(0, 101)
    def verifica_sorteio(palpite, numero_sorteado):
            if palpite == numero_sorteado:
                print(f'PARABÉNS !! O número sorteado era {numero_sorteado}')
            if palpite < numero_sorteado:
                print('Tente um número maior')
            if palpite > numero_sorteado:
                print('Tente um número menor')
    try:    
        while True:           
            palpite = int(input('Digite seu palpite: '))
            verifica_sorteio(palpite, numero_sorteado)
            if palpite == numero_sorteado:
                break
    except ValueError:
        print('Digite um número inteiro válido')
    
    resposta = str(input('Deseja continuar jogando? (s/n) ')).lower().strip()[0]

    if resposta == 'n':
        print('Encerrando...')
        break
    elif resposta == 's':
        os.system('cls') #limpa o terminal :)
        print('-'*30)
    else:
        print('resposta inválida, o jogo será encerrado..')
        break



