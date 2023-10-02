'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

# Declara variáveis para armazenar os valores
maiorIndice = 0
codMaiorIndice = 0
menorIndice = 1000000
codMenorIndice = 0
totalVeiculos = 0
cidadesMenos2000 = 0
acidentesCidadesMenos2000 = 0 

# Coleta os valores
for _ in range (5):
    codigo = (input("Digite o codigo da cidade: "))
    veiculos = int(input("Digite o número de veículos de passeio: "))
    acidentes = int(input("Digite o número de acidentes: "))
    
    # Compara os valores e insere nas variáveis
    if acidentes > maiorIndice:
        maiorIndice = acidentes
        codMaiorIndice = codigo
    if acidentes < menorIndice:
        menorIndice = acidentes
        codMenorIndice = codigo
    
    # Incrementa o total
    totalVeiculos += veiculos
    
    # Compara se o valor é menor que 2000 e incrementa as variáveis
    if veiculos < 2000:
        cidadesMenos2000 += 1
        acidentesCidadesMenos2000 += acidentes

# Mostra os resultados
print (f'A cidade com maior num de acidentes foi a de código: {codMaiorIndice} com {maiorIndice} acidentes')
print (f'A cidade com menor num de acidentes foi a de código: {codMenorIndice} com {menorIndice} acidentes')
print (f'A média de veículos das cidades é de: {totalVeiculos / 5:.2f}')
print (f'A média de acidentes em cidades < 2000 veículos foi de: {acidentesCidadesMenos2000 / cidadesMenos2000}')