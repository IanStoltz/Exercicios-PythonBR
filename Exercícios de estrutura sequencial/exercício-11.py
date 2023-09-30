'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''
# Coletando os valores dos números
inteiro = int(input("Insira um número inteiro: "))
inteiro1 = int(input("Insira mais um número inteiro: "))
real = float(input("Insira um número real: "))

# Calculando produto, soma e exponenciação
produto = (2 * inteiro) + (inteiro1 / 2)
soma = (3 * inteiro) + real
exponenciacao = (real**3)

# Mostrando os resultados
print(f'O produto do dobro do primeiro com metade do segundo é: {produto}')
print(f'A soma do triplo do primeiro com o terceiro é: {soma}')
print(f'O resultado do terceiro elevado ao cubo é: {exponenciacao}')