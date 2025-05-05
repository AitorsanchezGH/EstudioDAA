# Tenemos un vector (no ordenado) donde primero vienen los pares y luego los impares.
# Encontrar y devolver la posición del vector que contiene el último elemento par, con complejidad O(log n)

#Para conseguir O(log n) necesitamos descartar la mitad de la solución en cada llamada recursiva.



def DyV(vector):
    if (len(vector)==1):
        if (vector[0]%2==0):
            return 0
        else:
            return -1
    else:
        mitad = len (vector) // 2
        if (vector[mitad]%2!=0): #SI ES IMPAR
            return DyV(vector[0:mitad])
        else:
            pos = DyV(vector[mitad+1:])
            if (pos==-1):
                return mitad
            else:
                return pos + mitad + 1


vector=[4,2,6,18,8,7,9]
posicion = DyV (vector)
print(posicion)