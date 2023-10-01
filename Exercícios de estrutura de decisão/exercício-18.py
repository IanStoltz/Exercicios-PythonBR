'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

# Resolução por utilização do módulo datetime:, específico para lidar com datas.
# Se o código fosse resolvido com if else, ficaria muito extenso. O módulo tenta
# fazer o parsing da string usando o formato indicado, no caso %d/%m/%Y

# Coleta a data
data = str(input("Insira uma data no formato dd/mm/aaaa: "))

# Importa o módulo datetime
from datetime import datetime

# Declara função que verifica se a data é valida e mostra o resultado
def dataValida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        print ("Data válida")
    except ValueError:
        print ("Data inválida")

# Chama a função passando a data como argumento
dataValida(data)