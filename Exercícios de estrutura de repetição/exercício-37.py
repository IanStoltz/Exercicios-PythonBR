'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes
'''

# Declara variáveis para armazenar os valores
codAlto = 0
valorAlto = 0
codBaixo = 0
valorBaixo = 0
codGordo = 0
valorGordo = 0
codMagro = 0
valorMagro = 0
mediaAltura = 0
mediaPeso = 0
somaAltura = 0
somaPeso = 0
i = 1
vezes = 0

# Coletan código, altura, peso ou encerra o programa
while True:
    codigo = int(input('Digite seu código: '))
    if codigo == 0:
        break
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    # Compara os valores e atribui nas variáveis
    if i == 1:
        codBaixo = codigo
        valorBaixo = altura
        codMagro = 0
        valorMagro = 0
    if peso > valorGordo:
        codGordo = codigo
        valorGordo = peso
    if peso < valorGordo:
        codMagro = codigo
        valorMagro = peso
        
    if altura > valorAlto:
        codAlto = codigo
        valorAlto = altura
    if altura < valorBaixo:
        codBaixo = codigo
        valorBaixo = altura
    i += 1
    vezes += 1

    # Adiciona valores no total
    somaAltura += altura
    somaPeso += peso

# Caclula as médias    
mediaAltura = somaAltura / vezes
mediaPeso = somaPeso / vezes

# Mostra os resultados
print (f'O cliente mais baixo foi o de código {codBaixo}, com altura de {valorBaixo:.2f} m')
print (f'O cliente mais baixo foi o de código {codAlto}, com altura de {valorAlto:.2f} m')
print (f'O cliente mais leve foi o de código {codMagro}, com peso de {valorMagro:.2f} Kg')
print (f'O cliente mais pesado foi o de código {codGordo}, com peso de {valorGordo:.2f} Kg')
print(f'A média de peso foi de {mediaPeso:.2f} Kg, e de altura {mediaAltura:.2f} m')