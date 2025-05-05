# Estructura Union-Find
class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        rx = self.encontrar(x)
        ry = self.encontrar(y)
        if rx == ry:
            return False  # Ya están conectados
        if self.rango[rx] < self.rango[ry]:
            self.padre[rx] = ry
        else:
            self.padre[ry] = rx
            if self.rango[rx] == self.rango[ry]:
                self.rango[rx] += 1
        return True

# Lectura de entrada
n, m = map(int, input().split())

aristas = []
for _ in range(m):
    c1, c2, e = map(int, input().split())
    aristas.append((e, c1, c2))

# Kruskal
aristas.sort()  # Ordenamos por coste ascendente
uf = UnionFind(n)
esfuerzo_total = 0
esfuerzo_individual = [0] * n

for coste, a, b in aristas:
    if uf.unir(a, b):
        esfuerzo_total += coste
        esfuerzo_individual[a] += coste
        esfuerzo_individual[b] += coste

# Mostrar resultado
for i in range(n):
    print(f"C{i} -> {esfuerzo_individual[i]}")
print(f"Esfuerzo realizado -> {esfuerzo_total}")
