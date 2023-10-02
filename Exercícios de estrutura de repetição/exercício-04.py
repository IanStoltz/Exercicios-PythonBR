'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 
200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a 
população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

# Declara variáveis
paisA = 80000
paisB = 200000
crescimentoA = 0.03
crescimentoB = 0.015
anos = 0

# Verifica valores até que paisA ultrapasse ou iguale a população de paisB
while paisA <= paisB:
    anos += 1
    paisA += paisA * crescimentoA
    paisB += paisB * crescimentoB

# Mostra o resultado
print (f'Passarão {anos} anos até que o país A ultrapasse a população do país B')