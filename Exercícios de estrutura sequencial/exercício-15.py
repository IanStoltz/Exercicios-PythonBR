'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
1. salário bruto.
2. quanto pagou ao INSS.
3. quanto pagou ao sindicato.
4. o salário líquido.
5. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

# Coletando valores
valorPorHora = float(input("Quanto você recebe por hora trabalhada? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou este mês? "))

# Calculando salário e descontos
salarioBruto = valorPorHora * horasTrabalhadas
ir = (salarioBruto * 11) / 100
inss = (salarioBruto * 8) / 100
sindicato = (salarioBruto * 5) / 100
salarioLiq = salarioBruto - ir - inss - sindicato

# Mostrando os resultados
print (
    f'\n+ Salário Bruto : R$ {salarioBruto}'
    f'\n- IR (11%) : R$ {ir}'
    f'\n- INSS (8%) : R$ {inss}'
    f'\n- Sindicato (5%) : R$ {sindicato}'
    f'\n= Salário Líquido : R$ {salarioLiq}'
)