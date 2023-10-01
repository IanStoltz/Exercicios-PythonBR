'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
F - Feminino, M - Masculino, Sexo Inválido.
'''

# Coleta o valor do sexo
sexo = str(input("Qual o seu sexo? (M ou F): "))

# Compara o valor e mostra resultado
if sexo.upper() == "M":
    print("M - Masculino")
elif sexo.upper() == "F":
    print("F - Feminino")
else:
    print("Sexo inválido")