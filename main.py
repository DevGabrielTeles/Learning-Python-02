# Variables
dia_para_hora = 24
hora_para_minuto = 60
minuto_para_segundo = 60


# Function with if statement
def dia_para_segundos(num_dias):
    if num_dias == 1:
        return f"{num_dias} dia são {num_dias * dia_para_hora * hora_para_minuto * minuto_para_segundo} segundos"
    elif num_dias > 1:
        return f"{num_dias} dias são {num_dias * dia_para_hora * hora_para_minuto * minuto_para_segundo} segundos"
    elif num_dias == 0:
        return "Você inseriu um valor inválido, insira um valor positivo diferente de 0."
    else:
        return "Você inseriu um valor negativo."


# Validando dado string
def validacao():
    if total_dias.isdigit():
        funcao_calculada = dia_para_segundos(int(total_dias))
        # Calling function
        print(funcao_calculada)
    else:
        print("Não atrasa meu lado!")


# Input
total_dias = input("Digite o número de dias e te darei o total de segundos:")
validacao()
