def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

# Entrada desde consola
a, b = map(int, input().split())
print(mcd(a, b))
