from datetime import datetime

def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y").date()

def parsea_hora(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y %H:%M:%S")

def parsea_booleano(str_booleano):
    res = None
    if str_booleano == "S":
        res = True
    elif str_booleano == "N":
        res = False
    return res

def parsea_resultados(str_resultados):
 return [int(resultado) for resultado in str_resultados.split(",")]
