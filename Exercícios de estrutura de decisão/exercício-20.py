'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

# Declara a função que calcula a média
def calcular_media(parcial, parcial1, parcial2):
    media = (parcial + parcial1 + parcial2) / 3
    return media

# Declara a função que verifica a aprovação e mostra resultado
def verificar_aprovacao(media):
    if media == 10:
        return f'Aprovado com Distinção, sua média foi {media}'
    elif media >= 7:
        return f'Aprovado, sua média foi {media}'
    else:
        return f'Reprovado, sua média foi {media}'

# Coleta os valores das parciais
parcial = float(input("Insira sua nota da primeira parcial: "))
parcial1 = float(input("Insira sua nota da segunda parcial: "))
parcial2 = float(input("Insira sua nota da terceira parcial: "))

# Chama funções e armazena resultados nas respectivas variáveis
media = calcular_media(parcial, parcial1, parcial2)
resultado = verificar_aprovacao(media)

# Mostra o resultado
print(resultado)