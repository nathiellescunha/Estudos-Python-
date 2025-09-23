frase = str(input('Qual o seu nome completo?')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é {}'.format(frase.upper()))
print('Seu nome em letras minusculas é {}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
print('Seu primeiro nome tem ao todo {}'.format(frase.find(' ')))

#Crie um programa que lei nome completo de uma pessoa e mostre:
# O nome com todas as letras maisculas e minusculas
#Quantas letras tem ao todo sem considerar espaços usou oo strip e - frse.count
# quantas letras teve o primeiro nome