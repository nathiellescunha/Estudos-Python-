import random 
n1= str(input('Qual o primeiro nome?'))
n2= str(input('Qual o segundo nome?'))
n3= str(input('Qual o terceiro nome?'))
n4= str(input('Qual o quarto nome?'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno ecolhido foi {}'.format(escolhido))
