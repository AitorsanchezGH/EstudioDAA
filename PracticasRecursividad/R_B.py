def invertir(palabra):
    if len(palabra) <= 1:
        return palabra
    return invertir(palabra[1:]) + palabra[0]

# Lectura desde consola
entrada = input()
print(invertir(entrada))
