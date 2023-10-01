'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

# Coleta os valores dos lados
lado = float(input("Insira o primeiro lado: "))
lado1 = float(input("Insira o segundo lado: "))
lado2 = float(input("Insira o terceiro lado: "))

# Compara os valores, verifica se forma triângulo ou não, se sim, de qual tipo e mostra os resultados
if (lado + lado1) > lado2 and (lado1 + lado2) > lado and (lado + lado2) > lado1:
    print ("Forma triângulo")
    if lado == lado1 and lado1 == lado2:
        print ("Triângulo equilátero")
    elif lado != lado1 and lado1 != lado2 and lado != lado2:
        print ("Triângulo escaleno")
    else:
        print ("Triângulo isóceles")
else:
    print ("Não forma triângulo")