'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade
de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print ("Qual tipo de carne você irá levar? ")

# Coletando tipo, quantia e forma de pagamento
tipo = str(input("Filé, Alcatra ou Picanha: "))
quant = float(input("Quantos Kg de carne irá levar? "))
cartao = str(input("Vai pagar no cartao (s ou n)? "))

# Declarando preços
precoFile = 4.90
precoAlcatra = 5.90
precoPicanha = 6.90

# Verifica se a quantia é passível de desconto
if quant > 5: 
    precoFile = 5.80
    precoAlcatra = 6.80
    precoPicanha = 7.80

# Calcula preço total verificando o tipo
if tipo == "filé":
    precoTotal = quant * precoFile
elif tipo == "alcatra":
    precoTotal = quant * precoAlcatra
elif tipo == "picanha":
    precoTotal = quant * precoPicanha
else:
    print ("Tipo inválido")

# Mostra os resultados
print ("Cupom fiscal")
if cartao == "s":
    # Atribui desconto se pago no cartão
    precoDesc = 0.05 * precoTotal
    valorDesc = precoTotal - precoDesc
    print (f' Você comprou {quant} Kg de {tipo}, totalizando R$ {precoTotal:.2f}')
    print (f' Pagando no cartão há 5% de desconto, no valor de R$ {precoDesc:.2f}')
    print (f' O valor final ficou em R$ {valorDesc:.2f}')
else:
    print (f' Você comprou {quant} Kg de {tipo}, totalizando R$ {precoTotal:.2f}')