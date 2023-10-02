'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes 
aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o 
valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''

print('Lojas Tabajara')

# Declara variavel para armazenar o total e o número do produto
total = 0
produto = 1

# Coleta preço do produto ou encerra
while True:
    preco = float(input(f'Produto {produto}: R$ '))
    
    if preco == 0:
        break
    
    # Calcula total e incrementa o número do produto
    total += preco
    produto += 1

# Mostra o resultado total
print(f'Total de R$ {total:.2f}')

# Coleta o valor pago e calcula o troco
pagamento = float(input("Insira o valor pago pelo cliente: R$ "))
troco = pagamento - total

# Mostra o resultado
print(f'O troco é de R$ {troco:.2f}')