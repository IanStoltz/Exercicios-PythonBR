"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco
valores. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser
conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: [6.5, 6.1, 6.2, 5.4, 5.3]
Média dos saltos: 5.9 m
"""

# Declara lista para armazenar os atletas e define os saltos
atletas = []
saltos = "Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"

# Coleta nome dos atletas ou encerra o programa
while True:
    nome = input("Digite o nome do atleta (ou enter para encerrar o programa): ")
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
    }

    # Mostra o nome do atleta
    print(f'Atleta: {atleta.get("nome")}')

    # Calcula a média para cada atleta
    for i in range(5):
        atleta.get("saltos").append(float(input(f"{saltos[i]} salto: ")))
    atleta["media"] = sum(atleta.get("saltos")) / len(atleta.get("saltos"))

    # Insere o valor na lista
    atletas.append(atleta)

# Mostra os resultados para cada atleta
print("\nResultado final")
for atleta in atletas:
    print(
        f"Atleta: {atleta.get('nome')}\n"
        f"Saltos: {atleta.get('saltos')}\n"
        f"Média dos saltos: {atleta.get('media'):.1f} m\n"
    )
