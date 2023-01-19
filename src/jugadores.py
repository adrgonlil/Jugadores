from collections import namedtuple, defaultdict
import csv
from parsers import *

Jugador = namedtuple('Jugador', 'ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados')


def lee_jugadores(fichero):
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=";")
        next(lector)
        res=[]
        for ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados in lector:
            fecha_ncto=parsea_fecha(fecha_ncto)
            handicap = float(handicap) 
            fec_hor_act=parsea_hora(fec_hor_act)
            senior=parsea_booleano(senior)
            resultados=parsea_resultados(resultados)
            res.append(Jugador(ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados))
        return res


def mejores_jugadores(jugadores, anyo, n):
    
#recibe una lista de tuplas de tipo Jugador, un año y un número entero n, y devuelve una lista de tuplas con
#los números de licencia, apellidos y nombre y handicap de los n jugadores más buenos que nacieron en dicho año. (1 punto + 0,25 puntos el test).
    
    res=[]
    for j in jugadores:
        if anyo==j.fecha_ncto.year:
            res.append((j.licencia, j.ape_nom, j.handicap))
    res=sorted(res, key=lambda x:x[2])
    return res[:n]


def agrupar_por_numero_golpes(jugadores):
#recibe una lista de tuplas de tipo Jugador y devuelve una lista de tuplas con el número de golpes y
#asociado a dicho número un conjunto con los números de licencia de los jugadores que tienen ese número de golpes entre sus
#últimos resultados. La lista debe estar ordenada de mayor a menor número de golpes. (1,25 puntos + 0,25 por el test)  
    dicc=defaultdict(set)
    for j in jugadores:
        for resultado in j.resultados:
            dicc[resultado].add(j.licencia)
    return dicc

def jugadores_por_golpes(jugadores):
    d = agrupar_por_numero_golpes(jugadores)
    return sorted(d.items(), reverse=True)



def promedio_ultimos_resultados(jugadores, f1=None, f2=None):
#recibe una lista de tuplas de tipo Jugador y dos valores de tipo date f1 y f2, que por defecto pueden
#tomar el valor None, y devuelve una lista de tuplas con el número de licencia y el promedio de golpes de los últimos resultados de
#los jugadores de categoría senior (True), cuya fecha de actualización esté entre f1 y f2 (ambas inclusive). Si f1 es None, se tendrán
#en cuenta los jugadores con fecha de actualización anteriores a f2 (inclusive). Si f2 es None, se tendrán en cuenta los posteriores
#a f1 (inclusive). Si ambas son None, se tendrán en cuenta los registros de todos los jugadores. (1,5 puntos + 0,25 puntos el test)

    return [(j.licencia, promedio_golpes(j.resultados))for j in jugadores if en_fecha(j, f1, f2) and j.senior==True]

def en_fecha(jugador, f1, f2):
    res=False
    if f1 == None and f2 == None:
        res = True
    elif f1 == None:
        res = jugador.fec_hor_act.date()<=f2
    elif f2 == None:
        res = f1 <= jugador.fec_hor_act.date()
    else:
        res = f1 <= jugador.fec_hor_act.date() <= f2
    return res

def promedio_golpes(resultados):
    res = None
    if len(resultados)>0:
        res = sum(resultados)/len(resultados)
    return res

def jugador_menor_handicap_por_federacion(jugadores):
    dicc=defaultdict(list)
    for j in jugadores:
        dicc[j.federacion].append((j.ape_nom, j.handicap))
    for federacion, jugadores in dicc.items():
        dicc[federacion]=min(jugadores, key=lambda x:x[1])
    return dicc

def media_resultados(resultados):
    return sum(resultados) / len(resultados)

def func_aux_1(jugadores):
    dicc=defaultdict(list)
    for j in jugadores:
        handicaps=j.handicap
        dicc[handicaps].append(min(j.resultados))
    for handicap, resultados in dicc:
        dicc[handicap]=media_resultados(resultados)
    return dicc
    
def func_aux_2(d_promedios):
    promedios_ord=sorted(d_promedios.items())
    return [(f"{t1[0]} vs {t2[0]}", t1[1] - t2[1]) for t1, t2 in zip(promedios_ord, promedios_ord[1:])]



