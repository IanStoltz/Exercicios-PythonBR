'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''

# Coletando valor do lado do quadrado
lado = float(input("Insira o tamanho do lado do quadrado: "))

# Calculando a área e o dobro
area = lado ** 2
dobro = area * 2

# Mostrando o resultado
print (f'O dobro do valor da área é de: {dobro}')