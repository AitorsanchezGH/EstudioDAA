# Enunciado: Dado un vector, devolver el  mayor y el menor de sus elementos. Usando DyV
# [2, 1, 3, 8, 4, 10, 7, 6] -> 1 y 10

# División -> partir en 2.
# Conquista -> [a] con: mayor = a y menor = a.
# Combinación -> acto de fé (suponemos que ya funciona y devuelve lo que yo quiero bien)
# Mayor de la combinación es el mayor de los dos mayores e igual con los menores.

def DyV(vector,ini,fin):
    if (ini==fin):
        #Conquista
        return [vector[ini],vector[ini]]
    else:
        #División
        medio = (ini+fin)//2
        [menor1, mayor1] = DyV (vector, ini, medio)
        [menor2, mayor2] = DyV (vector, medio+1, fin)
        #Combinación
        menor = min(menor1, menor2)
        mayor = max(mayor1, mayor2)
        return [menor, mayor]


vector=[2,1,3,8,4,10,7,6]
[menor,mayor]=DyV (vector,0,len(vector)-1)
print("El mayor es: ", mayor)
print("El menor es: ", menor)



