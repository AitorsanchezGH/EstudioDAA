n = int(input())

for _ in range(n):
    cualidad = input()
    tiempo_max = int(input())
    t = int(input())

    personas = []
    for _ in range(t):
        datos = input().split()
        nombre = datos[0]
        b, i, k, t_seduccion = map(int, datos[1:])
        if cualidad == "beauty":
            valor = b
        elif cualidad == "intelligence":
            valor = i
        else:  # kindness
            valor = k
        ratio = valor / t_seduccion
        personas.append((nombre, valor, t_seduccion, ratio))

    # Ordenamos por ratio descendente
    personas.sort(key=lambda x: -x[3])

    seleccionados = []
    beneficio = 0.0
    tiempo_disponible = tiempo_max

    for nombre, valor, tiempo, _ in personas:
        if tiempo <= tiempo_disponible:
            seleccionados.append(nombre)
            beneficio += valor
            tiempo_disponible -= tiempo
        else:
            if tiempo_disponible > 0:
                fraccion = tiempo_disponible / tiempo
                beneficio += valor * fraccion
                seleccionados.append(nombre)
            break


    print(" ".join(seleccionados))
    print(f"{beneficio:.2f}")
