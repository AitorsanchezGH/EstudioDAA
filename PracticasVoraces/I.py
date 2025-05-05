from collections import deque

n = int(input())

for _ in range(n):
    m, k, c = map(int, input().split())

    # Creamos el grafo
    grafo = [[] for _ in range(k)]
    for _ in range(c):
        a, b = map(int, input().split())
        grafo[a].append(b)
        grafo[b].append(a)

    # BFS desde el concursante 0
    visitado = [False] * k
    profundidad = [0] * k
    cola = deque([0])
    visitado[0] = True

    fans = 1 if m >= 1 else 0

    while cola:
        actual = cola.popleft()
        if profundidad[actual] >= m - 1:
            continue
        for vecino in grafo[actual]:
            if not visitado[vecino]:
                visitado[vecino] = True
                profundidad[vecino] = profundidad[actual] + 1
                cola.append(vecino)
                fans += 1

    print(fans)
