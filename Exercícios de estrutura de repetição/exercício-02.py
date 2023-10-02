'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e 
voltando a pedir as informações.
'''

# Coleta os valores de usuário e senha
login = str(input("Insira um usuário: "))
senha = str(input("Insira uma senha: "))

# Compara se valores são iguais
while login == senha:
    print ("O login e a senha não podem ser iguais, digite novamente.")
    login = str(input("Insira um usuário: "))
    senha = str(input("Insira uma senha: "))

# Mostra o resultado
print("Cadastro aprovado")