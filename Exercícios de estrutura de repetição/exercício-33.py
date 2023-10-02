'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
 e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''

# Declara variáveis com inf, garantindo que os valores serão maiores e menores
maior = float('-inf')
menor = float('inf')
i = 1

# Coleta temperaturas ou encerrando o programa
while True:
    temperatura = float(input('Digite a temperatura ou -1 para encerrar: C° '))
    
    if temperatura == -1:
        break
    
    # Compara maiores e menores
    if i == 1:
        menor = temperatura
    
    if temperatura > maior:
        maior = temperatura
    
    if temperatura < menor:
        menor = temperatura
    
    i += 1

# Calcula a média
media = (maior + menor) / 2

# Mostra os resultados
print(f'Maior temperatura: C° {maior:.2f}')
print(f'Menor temperatura: C° {menor:.2f}')
print(f'A média foi de: C° {media:.2f}')