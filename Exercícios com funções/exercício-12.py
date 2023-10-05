"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""

# Importa random para utilizar shuffle
import random


# Declara função para embaralhar
def embaralhar_palavra(palavra):
    # Padroniza a palavra para caixa baixa
    palavra = palavra.lower()

    # Converte a palavra em uma lista de caracteres
    caracteres = list(palavra)

    # Embaralha os caracteres
    random.shuffle(caracteres)

    # Junta os caracteres embaralhados em uma nova palavra
    palavra_embaralhada = "".join(caracteres)
    return palavra_embaralhada


# Coleta a palavra
palavra = str(input("Insira uma palavra para embaralhar: "))

# Chama a função e armazena o resultado
palavra_embaralhada = embaralhar_palavra(palavra)

# Mostra o resultado
print(f"A palavra {palavra} emabaralhada ficou: {palavra_embaralhada}")
