'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera; necessita de limpeza; necessita troca do cabo ou conector; quebrado ou inutilizado 
Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

# Declaração de listas para armazenar as quantidades
situacoes = ["1 - Necessita de esfera", "2 - Necessita de limpeza", "3 - Troca do cabo ou conector", "4 - Quebrado ou inutilizado"]
esfera = []
limpeza = []
troca = []
quebrado = []
porcentagens = []
quantidade = []

# Mostrando as opções de input
print("Situação")
for situacao in situacoes: 
    print(situacao)

# Coletando situação dos mouses e inserindo nas listas
while True:
    num = int(input("Insira a situação do mouse: "))
    while num < 0 or num > 4:
        print("Número inválido")
        num = int(input("Insira a situação do mouse: "))
    if num == 0:
        break
    if num == 1:
        esfera.append(num)
    elif num == 2:
        limpeza.append(num)
    elif num == 3:
        troca.append(num)
    else:
        quebrado.append(num)

# Calculando total e porcentagens
total = len(esfera) + len(limpeza) + len(troca) + len(quebrado)
if total != 0:
    porc_esfera = (len(esfera) * 100) / total
    porc_limpeza = (len(limpeza) * 100) / total
    porc_troca = (len(troca) * 100) / total
    porc_quebrado = (len(quebrado) * 100) / total 
    quantidade.extend([len(esfera), len(limpeza), len(troca), len(quebrado)])
    porcentagens.extend([porc_esfera, porc_limpeza, porc_troca, porc_quebrado])

# Mostrando resultados
if total != 0:
    print(f'\nQuantidade de mouses: {total}')
    print(f'\nSituação              Quantidade            Percentual')
    for i, situacao in enumerate(situacoes):
        print(f'{situacao}       {quantidade[i]}            {porcentagens[i]}%')
