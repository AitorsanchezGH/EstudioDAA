n = int(input())
actividades = []

for _ in range(n):
    partes = input().split()
    nombre = partes[0]
    inicio = int(partes[1])
    fin = int(partes[2])
    actividades.append((nombre, inicio, fin))

# Ordenamos las actividades por tiempo de finalización
actividades.sort(key=lambda x: x[2])

contador = 0
fin_ultima = -1

for _, inicio, fin in actividades:
    if inicio >= fin_ultima:
        contador += 1
        fin_ultima = fin

print(contador)

