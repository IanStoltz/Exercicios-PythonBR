"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa. Para computar cada voto, a telefonista digitará um número, entre 1 e 23
correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os números e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. 
O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. 
O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. 
O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""
# Variáveis para armazenamento dos votos e total
votos = []
total_votos = 0


# Função que calcula o percentual dos votos
def calcular_percentual_votos(votos, total_votos):
    percentuais = {}
    for voto in votos:
        if voto not in percentuais:
            percentuais[voto] = votos.count(voto) / total_votos * 100
    return percentuais


print("Enquete: Quem foi o melhor jogador? ")

# Coleta do número do jogador e adição na lista de votos
while True:
    voto = int(input("Número do jogador (0=fim): "))
    if voto == 0:
        break
    while voto < 0 or voto > 23:
        print("Informe um valor entre 1 e 23 ou 0 para sair")
        voto = int(input("Número do jogador (0=fim): "))
    votos.append(voto)
    total_votos += 1

# Cálculo do percentual de votos chamando a função
percentuais = calcular_percentual_votos(votos, total_votos)

# Mostrando os resultados
if total_votos > 0:
    print("Resultado da votação: ")
    print(f"\nForam computados {total_votos} votos.")
    print(f"Jogador   |   Votos      |   % de votos   ")

    for jogador, percentual in percentuais.items():
        print(
            f"{jogador}         |    {votos.count(jogador)}         |   {percentual:.2f}"
        )

    # Calculando quem foi mais votado com base no percentual
    mais_votado = max(percentuais, key=percentuais.get)

    # Mostrando os resultados do jogador mais votado, com seu número de votos e percentual
    print(
        f"O melhor jogador foi o número {mais_votado}, com {votos.count(mais_votado)} votos, correspondendo a {percentuais[mais_votado]:.2f}% do total de votos"
    )
