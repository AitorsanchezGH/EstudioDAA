# Enunciado: Dado un vector de números, devolver las cifras en común de dichos números.
# [2341, 1523, 4812, 5132] -> 1 y 2
# Tipo de datos Solución (2341) -> [F, T, T, T, T, F, F, F, F, F ,F]

# División: partir en 2.
# Conquista: crear vector de T y F.
# Combinación -> acto de fé (suponemos que ya funciona y devuelve lo que yo quiero bien)
# Comparamos los dos vectores de booleanos y si coinciden en T,
# rellenamos a T dicha posición en el nuevo vector combinación.

def extraerCifras (numero):
    solucion = [False]*10

    while (numero>0):
        cifra = numero % 10
        numero = numero // 10
        solucion[cifra] = True
    return solucion

def combinar(sol1, sol2):
    solucion = [False]*10
    for i in range (len (sol1)):
        if (sol1[i]==True) and (sol2[i]==True):
            solucion[i] = True
    return solucion

def DyV (vector,ini,fin):
    if (ini==fin):
        cifras = extraerCifras (numeros[ini])
        return cifras
    else:
        medio = (ini+fin)//2
        solucion1 = DyV(vector,ini,medio)
        solucion2 = DyV(vector,medio+1,fin)
        solucion = combinar(solucion1,solucion2)
        return solucion

numeros = [2341, 1523, 4812, 5132]
solucion = DyV (numeros, 0, len(numeros)-1)

for i in range (len(solucion)):
    if(solucion[i]):
        print("Cifra en comun: ", i)
