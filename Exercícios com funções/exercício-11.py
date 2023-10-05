# Declara função que converte a data
def converter_data(data):
    # Verifica se a data é válida
    try:
        dia, mes, ano = map(int, data.split("/"))
        data_valida = True
    except ValueError:
        data_valida = False

    if data_valida:
        # Declara dicionário com os meses por extenso
        meses = {
            1: "janeiro",
            2: "fevereiro",
            3: "março",
            4: "abril",
            5: "maio",
            6: "junho",
            7: "julho",
            8: "agosto",
            9: "setembro",
            10: "outubro",
            11: "novembro",
            12: "dezembro",
        }

        # Verifica se o mês é válido
        if mes in meses:
            mes_extenso = meses[mes]
            data_formatada = str(f"{dia} de {mes_extenso} de {ano}")
            return data_formatada
        else:
            return None
    else:
        return None


# Coleta a data
data = str(input("Insira uma data no formato DD/MM/AAAA: "))

# Chama a função e armazena o resultado
data_formatada = converter_data(data)

# Mostra o resultado
print(f"A data formatada é {data_formatada}")
