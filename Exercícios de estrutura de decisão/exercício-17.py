'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

# Coleta o ano
ano = int(input("Insira o ano para consultar: "))

# Confere se o ano é bissexto e mostra o resultado
if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
	print ("Ano bissexto")
else:
	print ("Ano normal")