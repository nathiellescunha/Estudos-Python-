from datetime import date 
b = int(input('Digite um ano? Coloque 0 para analisar o ano atual ' ))
if b == 0:
    b= date.today ().year
if b % 4 == 0 and b % 100 !=0 or b % 400 == 0:
    print('O ano {} é bissexto'.format(b))
else:
    print('O ano {} não é bissexto'.format(b))


#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.