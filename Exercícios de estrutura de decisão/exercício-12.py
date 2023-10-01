'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (a empresa deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''

# Coletando valores de horas trabalhadas e ganhos por hora
horas_trabalhadas = float(input("Insira quantas horas você trabalhou: "))
valor_hora = float(input("Insira quanto você ganha por hora: "))

# Calculando salario bruto e descontos
salario_bruto = horas_trabalhadas * valor_hora
desconto_inss = (salario_bruto * 10) / 100
desconto_sindicato = (salario_bruto * 3) / 100
desconto_fgts = (salario_bruto * 11) / 100

# Declara função que mostra os resultados
def calcular_folha_pagamento():
    print(f'Salário bruto: ({horas_trabalhadas}H * R$ {valor_hora}): R$ {salario_bruto}')
    print("Descontos:")
    print(f'Sindicato (3%): (-) R$ {desconto_sindicato}')
    print(f'INSS (10%): (-) R$ {desconto_inss}')
    print(f'FGTS (11%): R$ {desconto_fgts}')
    print(f'Total de descontos: R$ {total_descontos}')
    print(f'Salário líquido: R$ {salario_liquido}')

# Compara os valores dos salários, atribui os descontos e calcula o salário liq.
if salario_bruto < 900:
    porcentagem_ir = "0"
    desconto_ir = "Isento"
    total_descontos = desconto_sindicato + desconto_inss
    salario_liquido = salario_bruto - total_descontos
elif salario_bruto > 900 and salario_bruto <= 1500:
    porcentagem_ir = 5
    desconto_ir = (salario_bruto * porcentagem_ir) / 100
    total_descontos = desconto_sindicato + desconto_inss + desconto_ir
    salario_liquido = salario_bruto - total_descontos
elif salario_bruto > 1500 and salario_bruto <= 2500:
    porcentagem_ir = 10
    desconto_ir = (salario_bruto * porcentagem_ir) / 100
    total_descontos = desconto_sindicato + desconto_inss + desconto_ir
    salario_liquido = salario_bruto - total_descontos
elif salario_bruto > 2500:
    porcentagem_ir = 20
    desconto_ir = (salario_bruto * porcentagem_ir) / 100
    total_descontos = desconto_sindicato + desconto_inss + desconto_ir
    salario_liquido = salario_bruto - total_descontos 

# Chama função para mostrar os resultados
calcular_folha_pagamento()