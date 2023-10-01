'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

# Coleta os valores das notas
parcial = float(input("Insira sua nota da primeira parcial: "))
parcial1 = float(input("Insira sua nota da segunda parcial: "))

# Calcula a média
media = float(parcial + parcial1) / 2

# Declara função para aprovar ou reprovar e mostra o resultado
def funcaoAprovacao(parcial, parcial1):
    if media == 10:
        print ("Aprovado com Distinção")
    elif media >= 7:
        print ("Aprovado")
    else:
        print ("Reprovado")

# Chaman função para mostrar o resultado
funcaoAprovacao(parcial, parcial1)