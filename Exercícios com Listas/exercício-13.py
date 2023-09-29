"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: Janeiro, Fevereiro, . . . )
"""

# Declarando listas e variáveis
temperatura = []
meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]
media = 0
n = 0
acimaMedia = {}

# Coletando e armazenando as temperaturas
for i in range(len(meses)):
    temperatura.append(float(input(f"Insira a temperatura de {meses[n]}: ")))
    media += temperatura[i]
    n += 1

# Calculando a média das temperaturas
media = media / len(meses)

# Comparando temperaturas acima da média
for i in range(len(meses)):
    if temperatura[i] > media:
        acimaMedia.update({meses[i]: temperatura[i]})

# Mostrando os resultados
print(f"Média das temperaturas anuais: {media:.2f}")
print(f"Meses com temperatura acima da média: {acimaMedia}")
