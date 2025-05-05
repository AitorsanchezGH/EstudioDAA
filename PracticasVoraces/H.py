# Union-Find con compresión de caminos
class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        rx = self.encontrar(x)
        ry = self.encontrar(y)
        if rx != ry:
            self.padre[ry] = rx  # Unimos los conjuntos

# Lectura de entrada
n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    a, b = map(int, input().split())
    uf.unir(a, b)

# Contamos componentes distintas
componentes = set()
for i in range(n):
    componentes.add(uf.encontrar(i))

print(len(componentes))
