from math import hypot
co= float(input('Qual o comprimento do cateto oposto?'))
ca= float(input('Qual o comprimento do cateto adjacente?'))
hi = hypot(co,ca)
print( ' A hipotenusa mede {:.2f}'.format(hi))