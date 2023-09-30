'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
'''

# Coletando valor da altura
altura = float(input("Insira sua altura em metros: "))

# Calculando peso ideal
pesoIdeal = (72.7 * altura) - 58

# Mostrando resultado
print (f'Seu peso ideal é de: {pesoIdeal:.2f} kg')