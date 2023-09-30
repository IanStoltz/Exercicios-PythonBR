'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
# Importa math para arredondar caso necessário
import math

# Coleta o valor da área
area = int(input("Insira a área a ser pintada, em metros quadrados : "))

# Calcula o número de latas necessárias e o valor
latas = area / 54
valor = 80 * latas

# Mostra o resultado
print (f'Para a área de {area} metros quadrados serão necessárias {math.ceil(latas)} lata(s) de 18 litros. Saindo por R$ {valor:.2f}')
