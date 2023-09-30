'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

# Coletando o valor em Celsius
celsius = float(input("Insira a temperatura em C°: "))

# Convertendo valor para Fahrenheit
conversao = (celsius * 9/5) + 32

# Mostrando o resultado
print (f'A temperatura de {celsius}°C convertida para Fahrenheit é {conversao}°F')