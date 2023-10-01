'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada 
valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e 
quatro notas de 1.
'''

# Coleta o valor que será sacado
valorSaque = int(input("Insira a quantia a ser sacada: "))

# Armazena o valor em uma variável pois ele será alterado para calcular as quantias
valorSaqueOrig = valorSaque

# Compara os valores, calcula a quantia de notas necessárias e mostra o resultado
if valorSaque > 10 and valorSaque <= 600:
    notas100 = int(valorSaque / 100)
    valorSaque = valorSaque - (notas100 * 100)
    notas50 = int(valorSaque / 50)
    valorSaque = valorSaque - (notas50 * 50)
    notas10 = int(valorSaque / 10)
    valorSaque = valorSaque - (notas10 * 10)
    notas5 = int(valorSaque / 5)
    valorSaque = valorSaque - (notas5 * 5)
    notas1 = int(valorSaque / 1)
    print (f'Valor sacado: R$ {valorSaqueOrig}')
    print (f' {notas100} notas de 100 \n {notas50} notas de 50 \n {notas10} notas de 10 \n {notas5} notas de 5 \n {notas1} notas de 1')
else:
    print("Valor Inválido")