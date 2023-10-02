'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve 
necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
'''

# Coleta o número que será multiplicado
numero = int(input('Montar a tabuada de: '))

# Coleta o intervalo da multiplicação
while True:
    comecar = int(input('Começar por: '))
    terminar = int(input('Terminar em: '))

    # Verifica se o número final não é menor que o inicial
    if comecar < terminar:
        break
    else:
        print('O número final deve ser maior do que o inicial. Digite novamente: ')
    
# Mostra os resultados
print(f'Vou montar a tabuada de {numero} começando em {comecar} e terminando em {terminar}:')
for i in range(comecar, terminar + 1):
    print(f'{numero} X {i} = {numero * i}')