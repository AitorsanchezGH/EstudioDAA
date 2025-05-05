# Hay que pensar en: que es la solución, que es la etapa y que es el intento.
# Solución: Tipo de variable para guardar la solución. Tablero en este caso.
# Etapa: Orden de trabajo. Cada BT hace un poquito. El número de fila a colocar en este caso.
# Intento: Distintas posibilidades de hacer mi orden de trabajo. 0..7 en este caso (las columnas).

def imprimir (tablero):
    for i in range (len (tablero)):
        for j in range (len (tablero[i])):
            print (tablero[i][j], end=" ")
        print("")

def BT(solucion, etapa, columnasUsadas, diagonales1Usadas, diagonales2Usadas):
    exito=False
    intento=0
    while(intento<8) and not exito:
        if not (intento in columnasUsadas) and not((etapa-intento) in diagonales1Usadas) and not((etapa+intento) in diagonales2Usadas):
            solucion[etapa][intento] = 'X'
            columnasUsadas.append(intento)
            diagonales1Usadas.append(etapa-intento)
            diagonales2Usadas.append(etapa + intento)
            if(etapa==7):
                exito=True
            else:
                exito= BT(solucion, etapa+1, columnasUsadas,diagonales1Usadas, diagonales2Usadas)

            if not exito:
                solucion[etapa][intento] = '-'
                columnasUsadas.remove(intento)
                diagonales1Usadas.remove(etapa - intento)
                diagonales2Usadas.remove(etapa + intento)
        intento+=1
    return exito

solucion =[]
for i in range(8):
    fila = ['-']*8
    solucion.append(fila)

columnasUsadas=[]
diagonales1Usadas=[]
diagonales2Usadas=[]
exito= BT(solucion, 0,columnasUsadas,diagonales1Usadas,diagonales2Usadas)
if (exito):
    imprimir(solucion)
else:
    print("No hay solucion.")

