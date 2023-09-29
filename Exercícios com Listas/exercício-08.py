"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
# Criando listas para armazenar os valores
idades = []
alturas = []

# Coletando valores e inserindo nas listas
for i in range(5):
    i += 1
    print(f"Pessoa {i}")
    idades.append(int(input("Insira a idade: ")))
    alturas.append(float(input("Insira a altura: ")))

# Mostrando os resultados
print(f" Idades inversas: {idades[::-1]}")
print(f" Alturas inversas: {alturas[::-1]}")
