n = int(input())
famosos = []

for _ in range(n):
    parts = input().split()
    nombre = parts[0]
    M = int(parts[1])
    L = int(parts[2])
    T = int(parts[3])
    ratio = L / M
    famosos.append((nombre, ratio, T))

# Ordenamos por mayor ratio
famosos.sort(key=lambda x: -x[1])

# Mostramos los nombres
for f in famosos:
    print(f[0])

# Buscamos el famoso con nombre alfabéticamente primero
alfabetico = min(famosos, key=lambda x: x[0])[0]

# Calculamos el tiempo que espera ese famoso
tiempo = 0
for f in famosos:
    if f[0] == alfabetico:
        break
    tiempo += f[2]

print(tiempo)








