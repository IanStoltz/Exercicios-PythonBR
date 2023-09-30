'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
- Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor.
'''

# Importando math para arredondar valores
import math

# Declarando variáveis
litrosLata = 18
litrosGalao = 3.6
precoLata = 80
precoGalao = 25

# Coletando valor da área a ser pintada
area = int(input("Insira a área a ser pintada, em metros quadrados : "))
litrosNecessarios = area / 6

# Calculando utilizando apenas latas e mostrando resultado
qtdLatas = math.ceil(litrosNecessarios / litrosLata)
custoLatas = qtdLatas * precoLata
print ("Somente latas: ")
print (f"O cliente precisará comprar {qtdLatas} latas, que custarão R$ {custoLatas}")

# Calculando utilizando apenas galões e mostrando resultado
qtdGaloes = math.ceil(litrosNecessarios / litrosGalao)
custoGaloes = qtdGaloes * precoGalao
print ("Somente galões: ")
print (f"O cliente precisará comprar {qtdGaloes} galões, que custarão R$ {custoGaloes}")

# Calculando utilizando latas e galões com 10% de folga
folga = litrosNecessarios * 1.1
qtdLatas1 = folga // litrosLata
litrosNecessariosFolga = folga - (qtdLatas1 * litrosLata)
qtdGaloes1 = math.ceil(litrosNecessariosFolga / litrosGalao)
custoLatasGaloes = (qtdLatas1 * precoLata) + (qtdGaloes1 * precoGalao)
print ("Latas e galões: ")
print (f"O cliente precisará comprar {qtdLatas1} latas e {qtdGaloes1} galões, que custarão R$ {custoLatasGaloes}")