'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará,
considerando um que a gasolina custe R$ 2,25 o litro. 
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''

# Declarando listas
veiculos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout"]
consumos = [7, 10, 12.5, 9, 14.5]
litros_totais = []
valores_totais = []

# Mostrando lista veículo / consumo
print("Comparativo de consumo de Combustível")

for i, veiculo in enumerate(veiculos):
    print(f'Veículo {i+1} \n Nome: {veiculo} \n Km por litro: {consumos[i]}')

# Calculando litros e valor para percorrer 1000km
for consumo in consumos:
    litros = 1000 / consumo
    litros_totais.append(litros)
    valor = litros * 2.25
    valores_totais.append(valor)

# Calculando quem roda mais por litro
idx_menor_consumo = consumos.index(max(consumos))
menor_consumo = veiculos[idx_menor_consumo]

# Mostrando relatório final
print("\nRelatório final")
for i, veiculo in enumerate(veiculos):
    print(f'{i+1} - {veiculo} - {consumos[i]} - {litros_totais[i]:.2f} litros - R$ {valores_totais[i]:.2f}')
print(f'O menor consumo é do {menor_consumo}')
