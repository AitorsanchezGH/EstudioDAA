import ast  # Para convertir string a lista

def contar_y_sumar(lista):
    if not lista:
        return (0, 0)

    cabeza, *cola = lista

    suma_cabeza = 0
    cantidad_cabeza = 0

    if isinstance(cabeza, int):
        suma_cabeza = cabeza
        cantidad_cabeza = 1
    elif isinstance(cabeza, list):
        suma_cabeza, cantidad_cabeza = contar_y_sumar(cabeza)

    suma_cola, cantidad_cola = contar_y_sumar(cola)

    return (suma_cabeza + suma_cola, cantidad_cabeza + cantidad_cola)

# Lectura de entrada
entrada = input()
cofres = ast.literal_eval(entrada)  # Convierte el string a lista segura

resultado = contar_y_sumar(cofres)
print(resultado)
