'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.'''

# Coletando valor em Fahrenheit
fahrenheit = float(input("Insira a temperatura em F°: "))

# Convertendo valor para Celsius
conversao = 5 * ((fahrenheit - 32)/9)

# Mostrando o resultado
print (f'A temperatura de {fahrenheit}°F convertida para Celsius é: {conversao}°C')