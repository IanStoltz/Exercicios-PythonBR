"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que 
passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma 
de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 
Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; 
A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""
# Declarando variáveis e listas para armazenar os valores
salarios = []
total_abonos = []
valor_abono = 0
funcionarios = 0
funcionarios_com_piso_abono = 0

print("Projeção de gastos com Abono")
print("============================")

# Coletando os salários e atribuindo piso do abono
while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    elif salario < 0:
        print("Insira um salário maior do que 0")
        salario = float(input("Salário: "))
    elif salario <= 500:
        funcionarios_com_piso_abono += 1
    salarios.append(salario)
    funcionarios += 1


# Função para calcular abono
def funcao_calcula_abono(salarios):
    dic_abonos = {}
    for salario in salarios:
        if salario <= 500:
            valor_abono = 100
        else:
            valor_abono = (salario * 20) / 100
        total_abonos.append(valor_abono)
        dic_abonos[salario] = valor_abono
    return dic_abonos


# Calculo do abono chamando a função
abonos = funcao_calcula_abono(salarios)

# Calculando maior valor de abono pago
maior_abono = max(abonos.values())

# Mostrando os resultados
print("\nSalário      -   Abono")

for salario, abono in abonos.items():
    print(f"R$ {salario}    -     R$ {abono}")

print(f"\nForam processados {funcionarios} colaboradores")
print(f"Total gasto com abonos R$ {sum(total_abonos)}")
print(f"Valor mínimo pago a {funcionarios_com_piso_abono} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono}")
