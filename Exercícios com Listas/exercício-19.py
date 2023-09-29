"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos 
válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor
da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

# Variáveis para armazenamento dos votos, total e contagem
votos = []
total_votos = 0
sistemas = ["Windows", "Unix   ", "Linux  ", "Netware", "Mac OS ", "Outro  "]
h = 0


# Função que calcula o percentual dos votos
def calcular_percentual_votos(votos, total_votos):
    percentuais = {}
    for voto in votos:
        if voto not in percentuais:
            percentuais[voto] = votos.count(voto) / total_votos * 100
    return percentuais


print("Qual o melhor Sistema Operacional para uso em servidores?")
print(
    "\n1- Windows Server"
    "\n2- Unix"
    "\n3- Linux"
    "\n4- Netware"
    "\n5- Mac OS"
    "\n6- Outro\n"
)

# Coleta do número do voto e adição na lista de votos
while True:
    voto = int(input("Número da resposta (0=fim): "))
    if voto == 0:
        break
    while voto < 0 or voto > 6:
        print("Informe um valor entre 1 e 6 ou 0 para sair")
        voto = int(input("Número do jogador (0=fim): "))
    votos.append(voto)
    total_votos += 1

# Cálculo do percentual de votos chamando a função
percentuais = calcular_percentual_votos(votos, total_votos)

# Mostrando os resultados
print(f"\nSistema Operacional   |   Votos      |   % de votos   ")
print("----------------------  ------------- -------------")
for sistema, percentual in percentuais.items():
    print(
        f"{sistemas[h]}               |    {votos.count(sistema)}         |   {percentual:.2f}"
    )
    h += 1
print("----------------------  ------------- ")
print(f"Total                      {total_votos}")

# Calculando quem foi mais votado com base no percentual
mais_votado = max(percentuais, key=percentuais.get)

# Mostrando os resultados do sistema mais votado, com seu número de votos e percentual
print(
    f"\nO Sistema Operacional mais votado foi o {sistemas[mais_votado-1]}, com {votos.count(mais_votado)} votos, correspondendo a {percentuais[mais_votado]:.2f}% do total de votos"
)
