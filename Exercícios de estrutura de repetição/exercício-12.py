'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

# Declara função tabuada
def tabuada():

    # Coleta o número
    num = int(input('Insira um número inteiro: '))
    
    # Verifica se o número é valido
    while num < 1 or num > 10:
        print("O número precisa ser de 1 a 10")
        num = int(input('Insira um número inteiro: '))

    # Mostra os resultados no intervalo proposto
    print(f'Tabuada do {num}: ')
    for multiplicador in range(1, 11):
        resultado = num * multiplicador
        print(f'{num} x {multiplicador} = {resultado}')

# Chama a função
tabuada()