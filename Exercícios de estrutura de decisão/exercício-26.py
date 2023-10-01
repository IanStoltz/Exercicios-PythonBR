'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

# Coleta o valor e o tipo de combustível que será abastecido
valor = float(input("Insira o valor a ser abastecido: "))
tipo = str(input("Qual o tipo de combustível desejado (A ou G)? "))

# Declara variável que armazena os preços
precoA = 1.90
precoG = 2.50

# Verifica o tipo, a quantia, atribui o desconto e preço a ser pago
if tipo == "A":
    litrosA = valor / precoA
    descontoA = (valor * 3) /100
    precoT = valor - descontoA
    if litrosA > 20:
        descontoA = (valor * 5) /100
        precoT = valor - descontoA
elif tipo == "G":
    litrosG = valor / precoG
    descontoG = (valor * 3) /100
    precoT = valor - descontoG
    if litrosG > 20:
        descontoG = (valor * 5) /100
        precoT = valor - descontoG
else:
    print ("Tipo inválido")

# Mostra os resultados
if tipo == "A":
    print (f'R$ {valor} de álcool dão {litrosA:.2f} l no preço de R$ {precoA}/l')
    if litrosA < 20:
        print (f'O desconto abaixo de 20l é de 3%, o desconto é de {descontoA}')
        print (f'O valor final é de R$ {precoT}')
    else: 
        print (f'O desconto acima de 20l é de 5%, o desconto é de {descontoA}')
        print (f'O valor final é de R$ {precoT}')
elif tipo == "G":
    print (f'R$ {valor} de gasolina dão {litrosG:.2f} l no preço de R$ {precoG}/l')
    if litrosG < 20:
        print (f'O desconto abaixo de 20l é de 3%, o desconto é de R$ {descontoG}')
        print (f'O valor final é de R$ {precoT}')
    else: 
        print (f'O desconto acima de 20l é de 5%, o desconto é de R$ {descontoG}')
        print (f'O valor final é de R${precoT}')