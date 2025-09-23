nome = str(input('Qual o seu nome?'))
if nome == 'Gustavo':
    print('que nome lindo você tem')
print('Bom dia,\033[0;32;43m {}\033'.format(nome))

        
        # esse que tá na esquerda sempre vai acontecer, agora o que esta dentro vai
        # acontecer somente quando, tivo o Gustavo.