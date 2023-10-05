"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor A para A.M. e P para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""


# Declara a função que converte as horas
def converter_horas(horas, minutos):
    if horas > 12:
        horas -= 12
        periodo = "P.M."
    else:
        periodo = "A.M."

    return horas, minutos, periodo


# Declara a função que exibe os resultados
def exibir_resultado(horas, minutos, periodo):
    print(f"A hora convertida é: {horas}:{minutos} {periodo}")


# Declara o loop de funcionamento
while True:
    # Coleta os valores
    horas = int(input("Digite as horas (formato de 24 horas): "))
    minutos = int(input("Digite os minutos: "))

    # Chama as funções
    hora_convertida, minutos_convertidos, periodo = converter_horas(horas, minutos)
    exibir_resultado(hora_convertida, minutos_convertidos, periodo)

    # Pergunta se irá repetir ou encerra o loop.
    repetir = input("Deseja converter outra hora? (S/N): ")
    if repetir.upper() != "S":
        break
