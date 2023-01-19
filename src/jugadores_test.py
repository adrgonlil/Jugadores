from jugadores import *
from datetime import datetime, date
def muestra_iterable(iterable):
    for elem in iterable:
        print(elem)

def test_lee_jugadores(jugadores):
    print(f"Registros leídos: {len(jugadores)}")
    print("Los dos primeros:")
    muestra_iterable(jugadores[:2])
    print("Los dos últimos:")
    muestra_iterable(jugadores[-2:])
    print()

def test_mejores_jugadores(jugadores):
    print("Test 2")
    print(mejores_jugadores(jugadores, 1969, 4))
    print()

def test_jugadores_por_golpes(jugadores):
    print("Jugadores por golpes")
    res = jugadores_por_golpes(jugadores)
    muestra_iterable(res, "\n")
    

def test_promedio_ultimos_resultados(jugadores, f1=None, f2=None):
    res = promedio_ultimos_resultados(jugadores, f1, f2)
    print(f"El promedio de cada jugador senior con fecha de actualización entre {f1} y {f2} es: \n")
    print(res)
    print()

def test_jugador_menor_handicap_por_federación(jugadores):
    res = jugador_menor_handicap_por_federacion(jugadores)
    print("Los mejores jugadores de cada federación son:")
    muestra_iterable(res.items())

def test_jugador_menor_handicap_por_federacion(jugadores):
    res = jugador_menor_handicap_por_federacion(jugadores)
    print("El mejor jugador por federación es:")
    muestra_iterable(res.items())

if __name__=="__main__":
    DATOS=lee_jugadores("./data/jugadores.csv")
    print("APARTADO A:")
    print(test_lee_jugadores(DATOS))
    print(test_mejores_jugadores(DATOS))
    print(jugadores_por_golpes(DATOS))
    test_promedio_ultimos_resultados(DATOS, date(2020,3,1), date(2020,5,31))
    test_jugador_menor_handicap_por_federación(DATOS)



