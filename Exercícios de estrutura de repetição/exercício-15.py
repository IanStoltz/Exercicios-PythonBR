'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n-ésimo termo'''

# Coleta o número de termos
termos = int(input("Digite o número de termos da série de Fibonacci: "))

# Declara variáveis para iniciar geração
numero_atual = 1
numero_anterior = 0

# Atualiza variáveis e mostra resultado atual
for _ in range(termos):
    print(numero_atual)
    numero_atual, numero_anterior = numero_atual + numero_anterior, numero_atual