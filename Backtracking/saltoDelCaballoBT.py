def imprimir(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print("")
solucion=[]
dim=5
for i in range(dim):
    fila=[0]*dim
    solucion.append(fila)
imprimir(solucion)
