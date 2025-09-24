sal = float(input('Quanto é o seu salário?'))
print(' Você ganha R$ {}, seu aumento esta sendo processado ....'.format(sal))
if sal <= 1.250:
    print(' Com um aumento de 10% pois, então ficara R$ {}'.format((sal * 0.10) + sal))
else:
    print(' Com um aumento de 15% pois, então ficara R$ {}'.format((sal * 0.15)+sal))

#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.