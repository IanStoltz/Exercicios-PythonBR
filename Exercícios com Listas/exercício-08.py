"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
# Cria listas para armazenar os valores
idades = []
alturas = []

# Coleta valores e inserindo nas listas
for i in range(5):
    pessoa = i + 1
    print(f"Pessoa {pessoa}")
    idade = int(input("Insira a idade: "))
    altura = float(input("Insira a altura: "))
    idades.append(idade)
    alturas.append(altura)

# Mostra os resultados
print(f"Idades inversas: {idades[::-1]}")
print(f"Alturas inversas: {alturas[::-1]}")
