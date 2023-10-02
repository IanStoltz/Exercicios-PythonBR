'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação 
e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as 
notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
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
        "notas": [],
        "media": 0,
        "melhor_nota": 0,
        "pior_nota": 0,
    }
    
    # Coleta nota das apresentações e insere na variável
    for i in range(7):
        atleta["notas"].append(float(input("Nota: ")))
    
    # Organiza as notas e remove a melhor e a pior
    atleta["notas"].sort()
    atleta["pior_nota"] = atleta["notas"].pop(0)
    atleta["melhor_nota"] = atleta["notas"].pop()
    atleta["media"] = sum(atleta["notas"]) / 5
    
    # Insere o atleta na lista de atletas
    atletas.append(atleta)

# Mostra o resultado de cada atleta
print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta['nome']}"
          f"\nMelhor nota: {atleta['melhor_nota']:.1f}"
          f"\nPior nota: {atleta['pior_nota']:.1f}"
          f"\nMédia: {atleta['media']:.1f}\n"
         )