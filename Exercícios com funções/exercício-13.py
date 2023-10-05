"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres + , − e |. 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
"""


# Declara função para desenhar a moldura com valor padrão
def desenha_moldura(linhas=1, colunas=1):
    # Ajusta os valores de linhas e colunas, se necessário
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    # Desenha a moldura
    print("+" + "-" * colunas + "+")
    for _ in range(linhas):
        print("|" + " " * colunas + "|")
    print("+" + "-" * colunas + "+")


# Chama a função e mostra o resultado
desenha_moldura(10, 20)
