def  todosNumerosIguales(matriz, iniFilas, finFilas, iniColumnas, finColumnas):
    aux=matriz[iniFilas][iniColumnas]
    for i in range(iniFilas, finFilas+1):
        for j in range(iniColumnas, finColumnas+1):
            if(matriz[i][j] != aux):
                return False
    return True

def DyV(matriz, iniFilas, finFilas, iniColumnas, finColumnas):
    if(iniFilas==finFilas) or todosNumerosIguales(matriz, iniFilas, finFilas, iniColumnas, finColumnas):
        return 1
    else:
        mitadFilas = (iniFilas+finFilas) // 2
        mitadColumnas = (iniColumnas+finColumnas) // 2
        n1=DyV(matriz,iniFilas,mitadFilas,iniColumnas,mitadColumnas)
        n2=DyV(matriz,iniFilas,mitadFilas,mitadColumnas+1,finColumnas)
        n3=DyV(matriz,mitadFilas+1,finFilas,iniColumnas,mitadColumnas)
        n4=DyV(matriz,mitadFilas+1,finFilas,mitadColumnas+1,finColumnas)
        return n1+n2+n3+n4


nFilas = int (input(""))
matriz = []
for i in range (nFilas):
    linea = input("")
    trozos = linea.split (" ")
    fila=[]
    for trozo in trozos:
        fila.append(int (trozo))
    matriz.append(fila)

num = DyV(matriz, 0, 3, 0, 3)
print(num)