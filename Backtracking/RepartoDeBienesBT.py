# Tenemos una empresa con unos bienes y sus dos socios se quieren separar.
# Debemos ofrecerles un reparto equitativo.

# Solución: Array paralelo al de los bienes. 0 nadie, 1 socio1, 2 socio2.
# Etapa: Indice en el array del objeto que toca repartir.
# Intento: Posibilidad de dárselo al socio1 o al socio2 (1 ó 2).
# Condiciones de factibilidad: Que un socio no tenga en su cuenta mas del 50%.

#Función factible se elimina al ser una condición

def BT(bienes, solucion, etapa, totalValor,cuentas):
    exito=False
    intento=1
    while(intento<=2) and not exito:
        #solucion[etapa]=intento??
        if (cuentas[intento-1]+bienes[etapa]<=(totalValor/2)):
            cuentas[intento-1]= cuentas[intento-1] + bienes[etapa]
            solucion[etapa]= intento
            if(etapa==len(bienes)-1):
                exito=True
            else:
                exito=BT(bienes,solucion,etapa+1, totalValor, cuentas)
            if not exito:
                solucion[etapa]=0
                cuentas[intento - 1] = cuentas[intento - 1] - bienes[etapa]
        intento=intento+1
    return exito

bienes=[40,20,25,5,10]
solucion=[0]*len(bienes)
#Contar valor de los bienes
totalValor = 0
for bien in bienes:
    totalValor = totalValor + bien

cuentas=[0,0] #Los contadores van dentro de arrays para poder modificarlos de llamada a llamada.
exito= BT(bienes, solucion, 0, totalValor, cuentas)
if (exito):
    print(bienes)
    print(solucion)
else:
    print("Con el valor de esos bienes y sin poderlos dividir, no hay posible reparto al 50%")