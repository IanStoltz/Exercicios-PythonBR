'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

# Declara função para calcular exponenciação
def calcular_potencia(base, expoente):
    potencia = 1
    for _ in range(expoente):
        potencia *= base
    return potencia

# Coleta os valores de base e expoente
base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))

# Chama a função e armazena o resultado na variável
resultado = calcular_potencia(base, expoente)

# Mostra o resultado
print(f'A base {base} elevada ao expoente {expoente} é: {resultado}')