'''
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente 
comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e 
olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços 
de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
---
50 - R$ 99.50
'''

# Coleta a quantia de produtos
quantidade_produtos = int(input("Insira a quantidade de produtos comprados: "))

# Itera a quantia de produtos, atribui o valor e mostra o resultado
print('Lojas Quase Dois - Tabela de preços')
for produto in range(1, quantidade_produtos + 1):
    resultado = produto * 1.99
    print(f'{produto} - R$ {resultado:1.2f}')