"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento,
que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero 
para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de p
restações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


# Declara função que calcula os valores
def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        valor_total = valor_prestacao + multa + juros
        return valor_total


# Declara variáveis para armazenar os valores
prestacoes_pagas = 0
valor_total_pagas = 0

# Declara o loop de funcionamento
while True:
    # Coleta o valor da prestação
    valor_prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))

    # Encerra o programa se o valor for 0
    if valor_prestacao == 0:
        break

    # Coleta os dias em atraso
    dias_atraso = int(input("Digite o número de dias em atraso: "))

    # Chama a função para calcular o valor e armazena em uma variável
    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)

    # Mostra o resultado e incrementa as prestações
    print("Valor a ser pago: R$", valor_a_pagar)
    prestacoes_pagas += 1
    valor_total_pagas += valor_a_pagar

# Mostra os resultados finais
print("Relatório do dia:")
print("Quantidade de prestações pagas:", prestacoes_pagas)
print("Valor total de prestações pagas: R$", valor_total_pagas)
