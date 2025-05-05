# Eliminar los elementos repetidos de un vector mediante una modificación en el algoritmo de MergeSort.

#Modificamos MergeSort en esta parte:

def DyV (vector, ini, fin):
    if (ini==fin):
        return [vector[ini]]
    else:
        mitad = (ini+fin)//2
        vectorMitad1 = DyV (vector, ini, mitad)
        vectorMitad2 = DyV (vector, mitad+1, fin)

        #MERGE
        nuevoVectorSalida=[]
        i=0
        j=0
        while (i<len(vectorMitad1)) and (j<len(vectorMitad2)):
            if (vectorMitad1[i]<vectorMitad2[j]):
                nuevoVectorSalida.append(vectorMitad1[i])
                i+=1
            elif(vectorMitad1[i]>vectorMitad2[j]):
                nuevoVectorSalida.append(vectorMitad2[j])
                j+=1
            else: #SON IGUALES
                nuevoVectorSalida.append(vectorMitad1[i])
                i+=1
                j+=1
        while (i<len(vectorMitad1)):
            nuevoVectorSalida.append(vectorMitad1[i])
            i+=1
        while (j<len(vectorMitad2)):
            nuevoVectorSalida.append(vectorMitad2[j])
            j+=1

        return nuevoVectorSalida

vector=[1,2,2,2,2,4,5,6]
nuevoVector = DyV(vector, 0, len(vector)-1)
print(nuevoVector)
