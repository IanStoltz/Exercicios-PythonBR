'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar 
uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''

# Coleta o valor da quantia pescada
peso = float(input("Insira a quantia pescada em kg: "))

# Compara o peso com o limite, calcula o excesso, a multa e mostra os resultados.
if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print (f'O excesso foi de {excesso} kg, sua multa é de R$ {multa:.2f}')
else:
	print ("Não houve excesso")
