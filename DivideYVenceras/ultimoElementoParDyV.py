# Tenemos un vector (no ordenado) donde primero vienen los pares y luego los impares.
# Encontrar y devolver la posición del vector que contiene el último elemento par, con complejidad O(log n)

#Para conseguir O(log n) necesitamos descartar la mitad de la solución en cada llamada recursiva.



def DyV(vector, ini, fin):
    if (ini==fin):
        if (vector[ini]%2==0):
            return ini
        else:
            return -1
    else:
        mitad = (ini+fin)//2
        if (vector[mitad]%2!=0): #SI ES IMPAR
            return DyV(vector, ini, mitad)
        else:
            pos = DyV(vector, mitad+1, fin)
            if (pos==-1):
                return mitad
            else:
                return pos


vector=[4,2,6,18,8,7,9]
posicion = DyV (vector, 0, len(vector)-1)
print(posicion)