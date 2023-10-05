"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado."""


# Declara função que contará os digitos
def contar_digitos(numero):
    return len(str(numero))


# Coleta o número
numero = int(input("Insira um número para saber sua quantia de dígitos"))

# Chama a função e armazena o resultado
contagem = contar_digitos(numero)

# Mostra o resultado
print(f"A quantia de dígitos do numero {numero} é de {contagem} dígitos.")
