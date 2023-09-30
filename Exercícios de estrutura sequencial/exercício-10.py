'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

# Coleta o valor em Celsius
celsius = float(input("Insira a temperatura em C°: "))

# Converte o valor para Fahrenheit
conversao = (celsius * 9/5) + 32

# Mostra o resultado
print (f'A temperatura de {celsius}°C convertida para Fahrenheit é {conversao}°F')
