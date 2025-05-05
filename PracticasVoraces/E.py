entradas = []

try:
    while True:
        linea = input()
        if linea.strip() == "":
            continue
        entradas.append(linea)
except EOFError:
    pass

indice = 0
v = int(entradas[indice])
indice += 1

for _ in range(v):
    p = int(entradas[indice])
    indice += 1

    datos = []
    while len(datos) < 2 * p:
        datos += list(map(int, entradas[indice].split()))
        indice += 1

    intervalos = []

    for i in range(p):
        inicio = datos[2 * i]
        fin = datos[2 * i + 1]
        intervalos.append((inicio, fin))

    intervalos.sort(key=lambda x: x[1])

    contador = 0
    fin_ultimo = -1

    for inicio, fin in intervalos:
        if inicio >= fin_ultimo:
            contador += 1
            fin_ultimo = fin

    print(contador)


