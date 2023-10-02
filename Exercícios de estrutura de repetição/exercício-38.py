'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

# Coleta o salário e o ano atual
salario = float(input("Digite o salário inicial do funcionário em 1995: "))
ano_atual = int(input("Digite em que ano estamos: "))

# Calcula o aumento
aumento = 1.5 / 100

# Itera no intervalo dos anos e incrementa os valores
for ano in range(1995, ano_atual + 1):
    salario *= 1 + aumento
    aumento *= 2

# Mostra o resultado
print(f"O salário em {ano_atual} é de R$ {salario:.2f}")