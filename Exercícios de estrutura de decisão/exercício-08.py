'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''

# Coleta os valores dos produtos
produto = float(input("Insira o preço do primeiro produto: R$ "))
produto1 = float(input("Insira o preço do segundo produto: R$ "))
produto2 = float(input("Insira o preço do terceiro produto: R$ "))

# Compara os preços e mostra o resultado
if produto < produto1 and produto < produto2:
    print (f'O primeiro produto, custando R$ {produto} é o mais barato')
elif produto1 < produto and produto1 < produto2:
    print (f'O segundo produto, custando R$ {produto1} é o mais barato')
elif produto2 < produto and produto2 < produto1:
    print (f'O terceiro produto, custando R$ {produto2} é o mais barato')
else:
    print ("Os preços dos produtos são iguais")