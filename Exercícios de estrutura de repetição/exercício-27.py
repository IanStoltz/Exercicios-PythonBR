'''
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''

# Coleta o número de turmas e declara lista para armazenar a quantia de alunos
turmas = int(input("Quantas turmas são? "))
alunos_turmas = []

# Itera sobre as turmas e coleta a quantia de alunos
for turma in range(1, turmas + 1):
    print("Turma", turma)
    alunos = int(input("Quantos alunos na turma: "))
    
    # Verifica se o número de alunos é menor que 40
    while alunos > 40:
        print("Turma", turma, "[Uma turma pode ter somente até 40 alunos]")
        alunos = int(input("Quantos alunos na turma: "))
    
    # Insere número de alunos na lista
    alunos_turmas.append(alunos)

# Calcula a média
media = sum(alunos_turmas) / len(alunos_turmas)

# Mostra o resultado
print(f'A média de alunos nas turmas é de: {media} alunos')