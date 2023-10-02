'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
# Coleta nome, compara se é válido e mostra o resultado
nome = str(input("Insira um nome: "))
while len(nome) < 3:
    print ("O nome precisa ter mais de 3 caracteres")
    nome = str(input("Insira um nome: "))
print ("Nome regristrado")

# Coleta idade, compara se é válida e mostra o resultado
idade = int(input("Insira sua idade: "))
while (idade <= 0) or (idade >= 150):
    print ("A idade precisa estar entre 0 e 150")
    idade = int(input("Insira sua idade: "))
print ("Idade registrada")

# Coleta o salário, compara se é válido e mostra o resultado
salario = int(input("Insira seu salário em R$ "))
while salario < 0:
    print ("O salário precisa ser maior ou igual a zero")
    salario = int(input("Insira seu salário em R$ "))
print ("Salário registrado")

# Coleta o sexo, compara se é válido e mostra o resultado
sexo = str(input("Insira seu sexo (m ou f): "))
while sexo != "m" and sexo != "f":
    print ("Você deve inserir m ou f como resposta")
    sexo = str(input("Insira seu sexo (m ou f): "))
print ("Sexo registrado")

# Coleta o estado civil, compara se é válido e mostra o resultado
estado = str(input("Insira seu estado civil (s, c, v, d)"))
while estado != "s" and sexo != "c" and sexo != "v" and sexo != "d":
    print ("Você deve inserir s, c, v ou d")
    estado = str(input("Insira seu estado civil (s, c, v, d)"))
print ("Estado civil registrado")