#Creacion de una matriz como lista de lista
import numpy as np
x =np.zeros(5,5)
print(x)
x += np.arange(5)
print(x)

def crear_matriz(numero_filas, numero_columnas):
    matriz = [None] * numero_filas
    for i in range(numero_filas):
        matriz[i] = [None] * numero_columnas
    

def dibujar_matriz(m3):
    print("La matriz es: ")
    for i in range(len(m3)):
        print(m3[i])

matriz = [[1,2,4],[2,3,5],[8,5,9],[1,2,3], [4,5,6]]
dibujar_matriz(matriz)

