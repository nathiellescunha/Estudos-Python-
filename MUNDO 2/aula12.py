nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('que nome bonito')
elif nome == 'Maria' or nome == 'João' or nome == 'Lucas':
     print ('Seu nome é bem normal no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))

