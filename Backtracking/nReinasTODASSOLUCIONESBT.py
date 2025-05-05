# Hay que pensar en: que es la solución, que es la etapa y que es el intento.
# Solución: Tipo de variable para guardar la solución. Tablero en este caso.
# Etapa: Orden de trabajo. Cada BT hace un poquito. El número de fila a colocar en este caso.
# Intento: Distintas posibilidades de hacer mi orden de trabajo. 0..7 en este caso (las columnas).

def imprimir (tablero):
    for i in range (len (tablero)):
        for j in range (len (tablero[i])):
            print (tablero[i][j], end=" ")
        print("")

def esFactible(solucion, etapa, intento):
    #solucion[etapa][intento]='X'????
    #Comprobamos en la columna intento que no tengamos otra X en una fila superior.
    for i in range (etapa):
        if(solucion[i][intento]=='X'):
            return False
    #Comprobamos diagonal 1
    fila = etapa-1
    columna = intento-1
    while(fila>=0and(columna>=0)):
        if(solucion[fila][columna]=='X'):
            return False
        fila-=1
        columna-=1
    # Comprobamos diagonal 2
    fila = etapa - 1
    columna = intento + 1
    while (fila >= 0 and (columna <= 7)):
        if (solucion[fila][columna] == 'X'):
            return False
        fila -= 1
        columna += 1
    return True

def BT(solucion, etapa):
    intento=0
    while(intento<8):
        #solucion[etapa][intento]='X' ?? hay algun problema de hacer esto? llamamos a esFactible.
        if esFactible(solucion, etapa, intento):
            solucion[etapa][intento] = 'X'
            #imprimir(solucion)
            #print("PULSA ENTER")
            #input("")
            if(etapa==7):
                imprimir(solucion)
                print("SOLUCION ENCONTRADA. PULSA ENTER PARA CONTINUAR.")
                input("")
            else:
                BT(solucion, etapa+1)
            solucion[etapa][intento] = '-'
        intento+=1


solucion =[]
for i in range(8):
    fila = ['-']*8
    solucion.append(fila)

BT(solucion, 0)

