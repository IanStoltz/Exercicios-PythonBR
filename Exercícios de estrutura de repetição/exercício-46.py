'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe 
a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
'''

# Declara lista para armazenar atletas
atletas = []

# Coleta nome do atleta ou encerra o programa
while True:
    nome = input("Digite o nome do atleta (ou pressione Enter para encerrar o programa): ")

    if nome == "":
        break
    
    # Declara dicionário para armazenar variáveis
    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhor_salto": 0,
        "pior_salto": 0,
    }

    # Coleta distância dos saltos e insere na variável
    for i in range(5):
        distancia_salto = float(input(f"Distância do {i+1}º salto: "))
        atleta["saltos"].append(distancia_salto)

    # Organiza os saltos e remove o melhor e o pior
    atleta["saltos"].sort()
    atleta["pior_salto"] = atleta["saltos"].pop(0)
    atleta["melhor_salto"] = atleta["saltos"].pop()
    atleta["media"] = sum(atleta["saltos"]) / 3

    # Mostra os resultados
    print(
        f"\nAtleta: {atleta['nome']}"
        f"\nMelhor salto: {atleta['melhor_salto']:.1f} m"
        f"\nPior salto: {atleta['pior_salto']:.1f} m"
        f"\nMédia dos demais saltos: {atleta['media']:.1f} m\n"
    )

    # Insere o atleta na lista de atletas
    atletas.append(atleta)

# Mostra o resultado de cada atleta
print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta['nome']}: {atleta['media']:.1f} m")