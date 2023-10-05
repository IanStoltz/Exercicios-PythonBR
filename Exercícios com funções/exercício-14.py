"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, 
colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
"""

# Esse foi complicado

# Importa itertools para gerar combinações
import itertools


# Declara a função para procurar os quadrados
def is_quadrado_magico(matriz):
    # Verifica se a soma das linhas, colunas e diagonais é a mesma
    soma = sum(matriz[0])
    for i in range(1, len(matriz)):
        if sum(matriz[i]) != soma:
            return False
    for j in range(len(matriz[0])):
        if sum(matriz[i][j] for i in range(len(matriz))) != soma:
            return False
    if sum(matriz[i][i] for i in range(len(matriz))) != soma:
        return False
    if sum(matriz[i][len(matriz) - i - 1] for i in range(len(matriz))) != soma:
        return False
    return True


# Declara a função para gerar e armazenar os quadrados no intervalo de números proposto
def gerar_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrados_magicos = []

    # Gera todas as combinações possíveis dos números de 1 a 9
    permutacoes = itertools.permutations(numeros)

    # Para cada combinação, acha os quadrados
    for permutacao in permutacoes:
        matriz = [list(permutacao[:3]), list(permutacao[3:6]), list(permutacao[6:])]
        if is_quadrado_magico(matriz):
            quadrados_magicos.append(matriz)

    # Mostra os quadrados mágicos encontrados
    for quadrado in quadrados_magicos:
        for linha in quadrado:
            print(linha)
        print()


gerar_quadrados_magicos()
