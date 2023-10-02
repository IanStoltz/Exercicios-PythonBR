'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

# Coleta número de eleitores e declara lista para armazenar os votos
eleitores = int(input("Digite o número de eleitores: "))
votos = []

# Coleta votos de acordo com o num. de eleitores, verifica o valor e os insere na lista
for i in range(eleitores):
    voto = int(input("Qual candidato deseja votar? [1, 2, 3]: "))
    while voto < 0 or voto > 3:
        print("Valor inválido")
        voto = int(input("Qual candidato deseja votar? [1, 2, 3]: "))
    votos.append(voto)

# Calcula a quantia de votos de cada candidato
quantidade_votos_candidato_1 = votos.count(1)
quantidade_votos_candidato_2 = votos.count(2)
quantidade_votos_candidato_3 = votos.count(3)

# Mostra os resultados
print("Quantidade de votos para candidato 1: ", quantidade_votos_candidato_1)
print("Quantidade de votos para candidato 2: ", quantidade_votos_candidato_2)
print("Quantidade de votos para candidato 3: ", quantidade_votos_candidato_3)