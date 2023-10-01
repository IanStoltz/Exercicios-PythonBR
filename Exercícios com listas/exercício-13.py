"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: Janeiro, Fevereiro, . . . )
"""

# Declara listas e variáveis
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

# Coleta e armazena as temperaturas
for mes in meses:
    temperatura.append(float(input(f"Insira a temperatura de {mes}: ")))
    media += temperatura[-1]

# Calcula a média das temperaturas
media = media / len(meses)

# Verifica temperaturas acima da média
acimaMedia = {mes: temp for mes, temp in zip(meses, temperatura) if temp > media}

# Mostra os resultados
print(f"Média das temperaturas anuais: {media:.2f}")
print(f"Meses com temperatura acima da média: {acimaMedia}")
