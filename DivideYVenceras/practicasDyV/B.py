def contar_inversiones(arr):
    def merge_sort(lista):
        if len(lista) <= 1:
            return lista, 0  # Lista ordenada y sin inversiones

        medio = len(lista) // 2
        izquierda, inv_izq = merge_sort(lista[:medio])
        derecha, inv_der = merge_sort(lista[medio:])
        combinada, inv_merge = merge(izquierda, derecha)
        return combinada, inv_izq + inv_der + inv_merge

    def merge(izq, der):
        resultado = []
        i = j = inv_count = 0

        while i < len(izq) and j < len(der):
            if izq[i] <= der[j]:
                resultado.append(izq[i])
                i += 1
            else:
                resultado.append(der[j])
                inv_count += len(izq) - i  # Cuenta las inversiones
                j += 1

        resultado += izq[i:]
        resultado += der[j:]
        return resultado, inv_count

    _, total_inversiones = merge_sort(arr)
    return total_inversiones

n = int(input())
puntuaciones = list(map(int, input().split()))
print(contar_inversiones(puntuaciones))



