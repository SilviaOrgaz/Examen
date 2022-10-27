#Creacion de una matriz como lista de lista
def crear_matriz(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [None] * numero_columnas
