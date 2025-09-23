print('Analisador de triângulos ...')
r1 = float(input('Qual o primeiro tamanho?'))
r2= float(input('Qual o segundo tamanho?'))
r3 = float(input('Qual o terceiro tamanho?'))
if r1 < r2 + r3 and r2 < r1 and r3 < r1 + r2:
    print('Os tamanhos formam um triangulo')
else:
    print('Os tamanhos não formam um triangulo')

#Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.