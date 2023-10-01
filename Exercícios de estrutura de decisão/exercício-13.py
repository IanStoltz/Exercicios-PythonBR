'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido.
'''

# Coleta o valor
num = int(input("Insira um número: "))

# Declara dicionário com valores e dia da semana correspondente
dias_semana = {
    1: "segunda-feira",
    2: "terça-feira",
    3: "quarta-feira",
    4: "quinta-feira",
    5: "sexta-feira",
    6: "sábado",
    7: "domingo"
}

# Verifica se o valor é valido e mostra o resultado
if num in dias_semana:
    print(f"O dia correspondente é {dias_semana[num]}")
else:
    print("Valor inválido")