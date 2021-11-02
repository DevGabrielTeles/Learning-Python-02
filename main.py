# Variables
dia_para_hora = 24
hora_para_minuto = 60
minuto_para_segundo = 60


# Function with if statement
def dia_para_segundos(num_dias):
    return f"{num_dias} dia(s) são {num_dias * dia_para_hora * hora_para_minuto * minuto_para_segundo} segundos"


# Validando dado string
def validacao():
    try:

        total_dias = int(user_input)
        if total_dias > 0:
            calculo = dia_para_segundos(total_dias)
            print(calculo)
        elif total_dias == 0:
            print("Você inseriu um valor inválido, insira um valor positivo diferente de 0.")
        elif total_dias < 0:
            print("Você inseriu um valor inválido, insira um valor positivo diferente de 0.")


    except ValueError:
        print("Não tente burlar a entrada.")


# Input
user_input = input("Digite o número de dias e te darei o total de segundos:")
validacao()
