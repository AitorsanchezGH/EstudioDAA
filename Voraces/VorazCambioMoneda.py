def imprimir(tiposDeMoneda, solucion):
    valorTotal = 0
    for i in range (len(tiposDeMoneda)):
        print(solucion[i], "unidades de valor: ", tiposDeMoneda[i])
        valorTotal += solucion[i] * tiposDeMoneda[i]
    print("El valor total es: ", valorTotal)

def voraz(tiposDeMoneda, cambio, solucion):
    index = 0
    while(cambio>0) and index<len(tiposDeMoneda):
        if(cambio>=tiposDeMoneda[index]):
            solucion[index]+=1
            cambio=cambio - tiposDeMoneda[index]
        else:
            index+=1

linea = input("")
trozos = linea.split(" ")
tiposDeMoneda = []
for trozo in trozos:
    tiposDeMoneda.append(int(trozo))
cambio = int (input(""))

solucion = [0]*len (tiposDeMoneda)

voraz(tiposDeMoneda, cambio, solucion)
imprimir(tiposDeMoneda, solucion)

