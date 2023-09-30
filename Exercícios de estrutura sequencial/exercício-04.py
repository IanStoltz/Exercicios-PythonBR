'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

# Coleta as notas
nota1 = float(input("Insira sua primeira média: "))
nota2 = float(input("Insira sua segunda média: "))
nota3 = float(input("Insira sua terceira média: "))
nota4 = float(input("Insira sua última média: "))

# Calcula a média
mediaFinal = (nota1 + nota2 + nota3 + nota4) / 4

# Mostra o resultado
print("Sua média final é de: ", mediaFinal)
