def buscar_posicion(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado


n = int(input())
grupo1 = list(map(int, input().split()))
m = int(input())
grupo2 = list(map(int, input().split()))
p = int(input())
parejas = [tuple(map(int, input().split())) for _ in range(p)]

# Procesamiento
for persona1, persona2 in parejas:
    pos1 = buscar_posicion(grupo1, persona1)
    pos2 = buscar_posicion(grupo2, persona2)

    if pos1 != -1 and pos2 != -1:
        print(f"{pos1} {pos2}")
    else:
        print("SIN DESTINO")
