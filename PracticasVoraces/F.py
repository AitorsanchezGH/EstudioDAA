import heapq

n, m = map(int, input().split())

# Grafo como lista de adyacencia
grafo = [[] for _ in range(n)]

for _ in range(m):
    c1, c2, d = map(int, input().split())
    grafo[c1].append((c2, d))
    grafo[c2].append((c1, d))  # porque las conexiones son bidireccionales

inicio, fin = map(int, input().split())

# Dijkstra
distancia = [float('inf')] * n
anterior = [-1] * n
distancia[inicio] = 0

cola = [(0, inicio)]  # (distancia acumulada, nodo)

while cola:
    dist, actual = heapq.heappop(cola)

    if dist > distancia[actual]:
        continue  # Ya tenemos una distancia mejor

    for vecino, peso in grafo[actual]:
        nueva_dist = distancia[actual] + peso
        if nueva_dist < distancia[vecino]:
            distancia[vecino] = nueva_dist
            anterior[vecino] = actual
            heapq.heappush(cola, (nueva_dist, vecino))

# Reconstruimos el camino
camino = []
actual = fin
while actual != -1:
    camino.append(actual)
    actual = anterior[actual]
camino.reverse()

# Resultado
print(distancia[fin])
print(" ".join(map(str, camino)))
