'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''

# Coleta o número
numero = float(input('Digite um número: '))

# Verifica se é inteiro ou decimal e mostra o resultado
if(numero == round(numero)):
    print(f'{int(numero)} é um número inteiro!')
else:
    print(f'{numero} é um número decimal!')