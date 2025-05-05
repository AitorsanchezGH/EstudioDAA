#BT Todas las soluciones, no tiene la variable éxito!!!

#Función factible se elimina al ser una condición

def BT(bienes, solucion, etapa, totalValor,cuentas):
    intento=1
    while(intento<=2) :
        #solucion[etapa]=intento??
        if (cuentas[intento-1]+bienes[etapa]<=(totalValor/2)):
            cuentas[intento-1]= cuentas[intento-1] + bienes[etapa]
            solucion[etapa]= intento
            if(etapa==len(bienes)-1):
                print(bienes)
                print(solucion)
                print("SOLUCION ENCONTRADA. REPARTO AL 50%. PULSA ENTER PARA CONTINUAR.")
                input("")
            else:
                BT(bienes,solucion,etapa+1, totalValor, cuentas)

            solucion[etapa]=0
            cuentas[intento - 1] = cuentas[intento - 1] - bienes[etapa]
        intento=intento+1

bienes=[40,20,25,5,10]
solucion=[0]*len(bienes)
#Contar valor de los bienes
totalValor = 0
for bien in bienes:
    totalValor = totalValor + bien

cuentas=[0,0] #Los contadores van dentro de arrays para poder modificarlos de llamada a llamada.
BT(bienes, solucion, 0, totalValor, cuentas)