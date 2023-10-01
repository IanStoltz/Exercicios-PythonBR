'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
ou “REPROVADO” se o conceito for D ou E.
'''

# Coleta os valores das notas
parcial = float(input("Insira a nota da primeira parcial: "))
parcial1 = float(input("Insira a nota da segunda parcial: "))

# Calcula a média
media = (parcial + parcial1) / 2

# Compara as médias e atribui conceitos
if media >= 9:
    conceito = "A"
    aprova = "APROVADO"
elif media >= 7.5:
    conceito = "B"
    aprova = "APROVADO"
elif media >= 6:
    conceito = "C"
    aprova = "APROVADO"
elif media >= 5:
    conceito = "D"
    aprova = "REPROVADO"
else:
    conceito = "E"
    aprova = "REPROVADO"

# Mostra os resultados
print(f'Nota da primeira parcial: {parcial}, nota da segunda parcial: {parcial1}')
print(f'A média é de: {media}, seu conceito é {conceito}')
print(f'Você foi {aprova}')