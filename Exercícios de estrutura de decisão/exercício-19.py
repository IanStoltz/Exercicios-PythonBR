'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

# Coleta o número
num = int(input("Insira um número: "))

# Armazena o número em uma variável pois ele será alterado para calcular os valores
numero_original = num

# Verifica se é um número válido, calcula os valores pedidos e armazena cada um em sua variável
if num > 1000:
    print("Insira um número menor que 1000")
else:
    unidades = num % 10
    num //= 10
    dezenas = num % 10
    num //= 10
    centenas = num

    # Mostra o resultado
    print(f'{numero_original} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades')