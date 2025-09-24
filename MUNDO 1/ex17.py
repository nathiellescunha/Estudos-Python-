d= int(input('Quantos dias o carro foi alugado?'))
k= float(input('Quantos km foi percorrido?'))
dia= 60 * d 
km= 0.15 * k
soma= dia + km
print(' O valor a ser pago é de R$ {}'.format(soma))