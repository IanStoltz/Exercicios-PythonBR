'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

# Coleta os números e o tipo de operação
numero = float(input("Digite um número: "))
numero1 = float(input("Digite outro número: "))
operacao = str(input("Digite o tipo de operação a ser realizado (+, -, /, *): "))

# Verifica o valor do tipo de operação e atribui a função da operação
if operacao == "+":
    resultado = numero + numero1
elif operacao == "-":
    resultado = numero - numero1
elif operacao == "/":
    resultado = numero / numero1
elif operacao == "*":
    resultado = numero * numero1
else:
    print ("Operação inválida")

# Executa a operação com base no valor inserido e mostra o resultado
if resultado % 2 == 0:
    print ("Número par")
else:
    print ("Número ímpar")
if resultado > 0:
    print ("Número positivo")
else:
    print ("Número negativo")
if (resultado == round(resultado)):
    print ("Número inteiro")
else:
    print ("Número decimal")
print ("O resultado é: ", resultado)