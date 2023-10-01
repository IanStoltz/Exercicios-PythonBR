"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um
valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça: Mostre a quantidade de valores que foram lidos; 
Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 
Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro; 
Calcule e mostre a soma dos valores; Calcule e mostre a média dos valores; 
Calcule e mostre a quantidade de valores acima da média calculada; 
Calcule e mostre a quantidade de valores abaixo de sete; 
Encerre o programa com uma mensagem;
"""
# Declara listas e variáveis
notas = []
acimaMedia = []
abaixoMedia = []

# Coleta as notas e armazena
while True:
    nota = float(input("Insira uma nota ou -1 para encerrar: "))
    if nota == -1:
        break
    else:
        notas.append(nota)

    # Calcula a soma e a média
    soma = sum(notas)
    media = sum(notas) / len(notas)

    # Atribui as notas em cada intervalo
    for i in range(len(notas)):
        if notas[i] > media:
            acimaMedia.append(notas[i])
        if notas[i] < 7:
            abaixoMedia.append(notas[i])

    # Atribui notas acima e abaixo da média
    acima = len(acimaMedia)
    abaixo = len(abaixoMedia)

    # Mostra os resultados
    print(f" Foram lidos {len(notas)} valores")
    print(f" A ordem inserida foi {notas}")
    print(f" A ordem inversa da inserida foi {notas[::-1]}")
    print(f" A soma dos valores inseridos é de: {soma}")
    print(f" A média dos valores inseridos é de: {media}")
    print(f" A quantia de valores acima da média é de: {acima}")
    print(f" A quantia de valores abaixo de 7 é de: {abaixo}")
    print("Programa encerrado")
