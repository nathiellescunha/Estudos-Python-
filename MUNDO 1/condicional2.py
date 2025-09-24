from random import randint
from time import sleep
computador = randint (0,5) # faz o jogador pensar 
print('vou pensar em um número de 0 a 5 tente adivinhar')

jogador = int(input(' Em que número eu pensei?'))   
print('ANALISANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você venceu')
else:
    print('Você errou, o número era {} computador venceu '.format(computador))
