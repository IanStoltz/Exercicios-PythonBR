'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

# Declara dicionário de candidatos
candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Clara"
}

# Declara dicionário de votos brancos e nulos
votos = {
    "nulo": 0,
    "branco": 0
}

# Declara dicionário para armazenar número de votos para cada valor no dicionário candidatos
votos_candidatos = {candidato: 0 for candidato in candidatos.values()}

# Mostra os candidatos e seus números
print("Candidatos:")
for numero, nome in candidatos.items():
    print(f"{numero} - {nome}")

# Mostra como sair, votar branco ou nulo
print("Digite 0 para sair, 5 para votar nulo ou 6 para votar em branco.")

# Coleta o voto
while True:
    voto = int(input("Insira o número do candidato: "))

    # Conferindo se o valor é valido, encerrando ou adicionando o voto ao respectivo dicionário
    if voto < 0 or voto > 6:
        print("Você inseriu um valor inválido.")
        voto = int(input("Insira o número do candidato, 5 para nulo ou 6 para branco: "))
    elif voto == 0:
        break
    else:
        if voto in candidatos:
            votos_candidatos[candidatos[voto]] += 1
        elif voto == 5:
            votos["nulo"] += 1
        else:
            votos["branco"] += 1

# Calcula o total de votos
total_votos = sum(votos_candidatos.values()) + votos["nulo"] + votos["branco"]

# Mostra os resultados
print("\nResultado da eleição:")
for candidato, votos in votos_candidatos.items():
    print(f"{candidato} teve {votos} votos, um total de {100 * votos / total_votos:.2f}%")
print(f"{votos['nulo']} votos foram anulados, um total de {100 * votos['nulo'] / total_votos:.2f}%")
print(f"{votos['branco']} votos foram em branco, um total de {100 * votos['branco'] / total_votos:.2f}%")
print(f"O total de votos foi de: {total_votos}")