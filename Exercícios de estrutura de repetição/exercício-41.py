'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

# Coleta o valor e declara variável para contar as parcelas
valorDivida = float(input("Digite o valor da dívida: "))
parcelas = 1

print("|Dívida     |Juros      |Parcelas   |Valor      ")

while True:
    juros = (5 / 3) * parcelas + 5
    
    if parcelas == 1:
        juros = 0
    
    # Calcula os valores
    valorJuros = valorDivida * (juros / 100)
    valorTotal = valorDivida + valorJuros
    valorParcela = valorTotal / parcelas
    
    # Mostra o resultado
    print(
        f"|R$ {valorTotal:.2f}\t"
        f"|R$ {valorJuros:.2f}\t"
        f"|{parcelas}\t\t\t"
        f"|R$ {valorParcela:.2f}"
    )
    
    # Verifica e incrementa o número de parcelas
    if parcelas == 1:
        parcelas -= 1
    
    parcelas += 3
    
    if parcelas > 12:
        break