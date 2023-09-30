'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps). 
Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

# Coleta os valores de tamanho do arquivo e velocidade da conexão
tamanho = float(input("Insira, em MB, o tamanho do arquivo que será baixado: "))
velocidade = float(input("Insira a velocidade da sua conexão em Mbps: "))

# Calcula o tempo necessário
tempo = (tamanho / velocidade) / 60

# Mostra o resultado
print(f"O tempo estimado de download de {tamanho} MB, a {velocidade} Mbps, é de {tempo} minutos")
