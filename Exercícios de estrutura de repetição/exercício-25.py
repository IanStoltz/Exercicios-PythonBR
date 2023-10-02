'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 
0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

# Declara função que calcula a média de idades
def calcular_media_idades():

    # Coleta o número de pessoas
    n = int(input("Digite o número de pessoas: "))
    
    # Declara lista para armazenar as idades
    todasAsIdades = []
    
    # Coleta os valores das idades e insere na lista
    for _ in range(n):
        idade = float(input("Digite a idade: "))
        todasAsIdades.append(idade)
    
    # Calcula a média
    media = sum(todasAsIdades) / n
    
    # Compara a média com os intervalos e mostra o resultado
    if media > 0 and media <= 25:
        print("Turma jovem")
    elif media > 25 and media <= 60:
        print("Turma adulta")
    elif media > 60:
        print("Turma idosa")

# Chama a função
calcular_media_idades()