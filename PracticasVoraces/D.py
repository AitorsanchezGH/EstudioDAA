n, k = map(int, input().split())
participantes = []

for _ in range(n):
    nombre, edad = input().split()
    participantes.append((nombre, int(edad)))

participantes.sort(key=lambda x: x[1])

# Opción 1: jóvenes = k más jóvenes
grupo1 = participantes[:k]
grupo2 = participantes[k:]
suma1 = sum(p[1] for p in grupo1)
suma2 = sum(p[1] for p in grupo2)
diff1 = abs(suma1 - suma2)

# Opción 2: jóvenes = k más mayores
grupo3 = participantes[-k:]
grupo4 = participantes[:-k]
suma3 = sum(p[1] for p in grupo3)
suma4 = sum(p[1] for p in grupo4)
diff2 = abs(suma3 - suma4)

# Elegimos la opción con mayor diferencia
if diff1 >= diff2:
    jovenes = grupo1
    mayores = grupo2
else:
    jovenes = grupo3
    mayores = grupo4

# Ordenamos ambos por edad
jovenes.sort(key=lambda x: x[1])
mayores.sort(key=lambda x: x[1])

# Comprobamos cuál es realmente el grupo más joven
if sum(p[1] for p in jovenes) <= sum(p[1] for p in mayores):
    print(" ".join(p[0] for p in jovenes))
    print(" ".join(p[0] for p in mayores))
else:
    print(" ".join(p[0] for p in mayores))
    print(" ".join(p[0] for p in jovenes))

