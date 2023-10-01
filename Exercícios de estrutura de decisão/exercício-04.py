'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

# Declara lista de vogais
vogais = ["a", "e", "i", "o", "u"]

# Coleta a letra
letra = str(input("Insira uma letra: "))

# Verifica se foi inserida uma letra

if letra.isalpha():

    # Verifica se a letra é uma vogal ou consoante e mostrando o resultado
    if letra in vogais:
        print("Você inseriu uma vogal")
    else:
        print("Você inseriu uma consoante")
else:
    print("Você não inseriu uma letra")