'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''

# Declara variável para armazenar os anos necessários
anos = 0

# Coleta e valida o valor da população do país A
paisA = int(input("Insira a população do país A: "))
while paisA < 0:
    print ("O valor da população precisa ser maior que 0")
    paisA = int(input("Insira a população do país A: "))
print ("Valor aceito")

# Coleta e valida o valor da população do país B
paisB = int(input("Insira a população do país B: "))
while paisB < 0:
    print ("O valor da população precisa ser maior que 0")
print ("Valor aceito")

# Coleta e valida a taxa de crescimento da população do país A
crescimentoA = int(input("Insira a taxa de crescimento do país A: "))
while crescimentoA < 0:
    print ("A taxa de crescimento precisa ser maior que 0")
    crescimentoA = float(input("Insira a taxa de crescimento do país A: "))
print ("Valor aceito")

# Coleta e valida a taxa de crescimento da população do país B
crescimentoB = float(input("Insira a taxa de crescimento do país B: "))
while crescimentoB < 0:
    print ("A taxa de crescimento precisa ser maior que 0")
    crescimentoA = int(input("Insira a taxa de crescimento do país B: "))
print ("Valor aceito")

# Verifica os valores até que paisA ultrapasse ou iguale a população de paisB
while paisA <= paisB:
    anos += 1
    paisA += paisA * (crescimentoA / 100)
    paisB += paisB * (crescimentoB / 100)

# Mostra o resultado
print (f'Passarão {anos} anos até que o país A ultrapasse a população do país B')