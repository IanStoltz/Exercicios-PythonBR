'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% 
sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago 
pelo cliente.
'''
# Coleta as quantias compradas
quantidade_morangos = int(input("Insira a quantidade, em Kg, de morangos: "))
quantidade_macas = int(input("Insira a quantidade, em Kg, de maçã: "))

# Declara variável que armazena o total e os preços
kgTotal = quantidade_morangos + quantidade_macas
precoMora = 2.50
precoMaca = 1.80

# Verifica a quantia e atribui valor com desconto se necessário
if quantidade_morangos > 5: 
    precoMora = 2.20
elif quantidade_macas > 5:
    precoMaca = 1.50

# Declara variável que armazena o valor total e o calcula
valorTotal = (quantidade_morangos * precoMora) + (quantidade_macas * precoMaca)

# Verifica o peso e valor total, atribui desconto e mostra o resultado
if kgTotal >= 8 or valorTotal >= 25:
    desconto = 0.1 * valorTotal
    valorTotal = valorTotal - desconto
    print (f'Você comprou {quantidade_morangos} Kg de morango e {quantidade_macas} Kg de maçãs')
    print (f'O preço com desconto de R$ {desconto: .2f} é de: R$ {valorTotal: .2f}')
else:
    print (f'Você comprou {quantidade_morangos} Kg de morango e {quantidade_macas} Kg de maçãs')
    print (f'O preço é de: R$ {valorTotal: .2f}')