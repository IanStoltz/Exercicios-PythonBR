'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que 
calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

# Coleta o valor do salário
salario = float(input("Insira o seu salário atual: R$ "))

# Declara a função que calcula o reajuste com base no salário
def calcular_reajuste(salario):
    if salario < 280:
        return 0, 0, salario
    elif salario <= 700:
        porcentagem = 15
    elif salario < 1500:
        porcentagem = 10
    else:
        porcentagem = 5
    
    reajuste = (salario * porcentagem) / 100
    salario_novo = reajuste + salario
    
    return porcentagem, reajuste, salario_novo

# Declara a função que mostra o resultado
def mostrar_salario(salario, porcentagem, reajuste, salario_novo):
    print(f'Seu salário antes do reajuste era de R$ {salario}')
    print(f'Após o reajuste de {porcentagem}%, o valor do aumento foi de R$ {reajuste}')
    print(f'Seu novo salário é de R$ {salario_novo}')

# Chama a função de reajuste e armazena o resultado nas respectivas variáveis
porcentagem, reajuste, salario_novo = calcular_reajuste(salario)

# Chama a função que mostra o resultado passando os parâmetros armazenados
mostrar_salario(salario, porcentagem, reajuste, salario_novo)