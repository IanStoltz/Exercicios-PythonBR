'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: 
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

# Declara a função
def somaImposto(taxaImposto, custo):
    taxa = (taxaImposto * custo) / 100
    custo = taxa + custo
    return custo

# Coleta os valores
custo = float(input("Insira o valor do item: "))
taxaImposto = int(input("Insira o valor do imposto sobre venda, em porcentagem: "))

# Armazena o resultado
resultado = somaImposto(taxaImposto, custo)
print(f'O valor do item após o cálculo do imposto é: R${resultado}')
