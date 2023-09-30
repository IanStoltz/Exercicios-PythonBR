'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 
Para homens: (72.7*h) - 58; Para mulheres: (62.1*h) - 44.7
'''

# Coletando sexo e altura
sexo = str(input("Entre seu sexo: (masculino ou feminino) "))
altura = float(input("Insira sua altura em metros: "))

# Calculando peso ideal masculino e feminino
pesoIdealM = (72.7 * altura) - 58
pesoIdealF = (62.1 * altura) - 44.7

# Classificando e mostrando resultado
if sexo.lower() == "masculino":
	print (f'Seu peso ideal é de: {pesoIdealM} kg')
elif sexo.lower() == "feminino":
	print (f'Seu peso ideal é de: {pesoIdealF} kg')