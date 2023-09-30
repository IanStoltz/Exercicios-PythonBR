'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
'''

# Coleta o valor da hora e o número de horas trabalhadas
valorPorHora = float(input("Quanto você recebe por hora trabalhada? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou este mês? "))

# Calcula o salário
salario = horasTrabalhadas * valorPorHora

# Mostra o resultado
print (f'Seu salário é de R$ {salario}')
