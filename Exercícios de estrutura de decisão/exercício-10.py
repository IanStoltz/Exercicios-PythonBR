'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

# Pergunta o turno e coleta seu valor
print("Qual é o seu turno?")
turno = str(input("M - Matutino, V - Vespertino ou N - Noturno: "))

# Verifica qual o turno e mostra o resultado
if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Turno inválido")