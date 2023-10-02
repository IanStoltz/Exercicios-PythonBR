'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''

# Mostra números no intervalo proposto
num = 0
while num <= 19:
    num += 1
    print (num)

# Adiciona números na lista para dispor lado a lado
num = 0
lista = []
while num <= 19:
    num += 1
    lista.append(num)

# Mostra números lado a lado    
print (lista)