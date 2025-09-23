p= float(input('Qual o valor do salário ? R$'))
a=0.15
b= p * a 
salario= p + b
print(' O salário é de R$ {:.2f}, com aumento de 15%   fica R$ {:.2f},'.format(p,salario))
