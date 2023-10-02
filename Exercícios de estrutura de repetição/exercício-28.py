'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

# Coleta a quantia de CD's e declara lista para armazenar o valor
cds = int(input("Digite quantos CDs você possui: "))
cdsLista = []

# Itera pela quantia total, coleta o valor de cada CD e insere na lista
for numCds in range(1, cds+1):
    print(f'CD de número: {numCds}')
    valorCD = float(input("Digite o valor do CD: R$ "))
    cdsLista.append(valorCD)

# Calcula a média
media = sum(cdsLista) / len(cdsLista)

# Mostra o resultado
print(f'A média de valor para cada CD é de: R$ {media}')