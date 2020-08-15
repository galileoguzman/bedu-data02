numeros = [3, 148, 74, 71, 4, 83, 95, 20, 61, 10, 69, 67, 23, 164, 97, 67, 144, 200, 38, 90, 200, 162, 6, 180, 65, 71, 90, 182, 16, 132, 182, 108, 90, 196, 48, 2, 158, 88, 39, 39, 54, 80, 89, 3, 90, 170, 88, 71, 142, 45, 81, 194, 36, 39, 30, 33, 38, 44, 134, 43, 12, 52, 170, 162, 192, 83, 18, 176, 120, 28, 86, 188, 51, 11, 96, 13, 198, 34, 66, 23, 200, 62, 194, 91, 51, 26, 152, 186, 86, 38, 46, 66, 83, 66, 40, 2, 20, 12, 91, 53]

def numero_par(numero):
    if numero % 2 == 0:
        return True

def numero_mayor_100(numero):
    if numero > 100:
        return True


# Filtrar y obtener los numeros pares de la lista numeros
numeros_pares = list(filter(numero_par, numeros))
# print(numeros_pares)

# Filtrtar y obtener los numeros mayores que 100
numeros_mayores_que_100 = list(filter(numero_mayor_100, numeros))
# print(numeros_mayores_que_100)


# La tienda pozole mio, quiere saber que porcentaje de productos es acredor a un descuento del 15%
# Solo los productos con IVA incluido que su valor sea mayor que 50 pero menor que 100 son acredores al descuento

def precio_con_iva(precio):
    return round(precio * 1.16, 2)

def precio_con_descuento(precio):
    if precio > 50 and precio < 100:
        return True

precios_sin_iva = [3, 148, 74, 71, 4, 83, 95, 20, 61, 10, 69, 67, 23, 164, 97, 67, 144, 200, 38, 90, 200, 162, 6, 180, 65, 71, 90, 182, 16, 132, 182, 108, 90, 196, 48, 2, 158, 88, 39, 39, 54, 80, 89, 3, 90, 170, 88, 71, 142, 45, 81, 194, 36, 39, 30, 33, 38, 44, 134, 43, 12, 52, 170, 162, 192, 83, 18, 176, 120, 28, 86, 188, 51, 11, 96, 13, 198, 34, 66, 23, 200, 62, 194, 91, 51, 26, 152, 186, 86, 38, 46, 66, 83, 66, 40, 2, 20, 12, 91, 53]
precios_con_iva = list(map(precio_con_iva, precios_sin_iva))
precios_con_descuento = list(filter(precio_con_descuento, precios_con_iva))
print(precios_con_descuento)
