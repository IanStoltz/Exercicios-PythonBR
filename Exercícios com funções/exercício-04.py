'''
Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.
'''

# Declara função 
def funcao(argumento):
    if argumento > 0:
        return "P"
    elif argumento == 0 or argumento < 0:
        return "N"
    
# Coleta o valor do argumento
argumento = int(input("Insira um valor para verificar se é P - positivo ou N - negativo: "))

# Chama a função e mostra o resultado
resultado = funcao(argumento)
print(f'O número inserido é {resultado}')
