"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado."""


# Declara a função
def reverso_numero(numero):
    return int(str(numero)[::-1])


# Coleta o número
numero = int(input("Insira um número para inverter a ordem: "))

# Chama a função e armazena o resultado
reverso = reverso_numero(numero)

# Mostra o resultado
print(f"O número {numero} na ordem inversa é {reverso}")
