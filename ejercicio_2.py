lista = [18, 50, 210, 80, 145, 333, 70, 30]

#Organiza la lista mediante el metodo de ordenamiento sort
lista.sort()
print(lista)

def imprimir_numero(lista):
    for i in lista:
        if i % 10 == 0 and i < 200:
            print (i)

imprimir_numero(lista)

def parar(lista):
    for i in lista:
        if i >= 300:
            break
        else:
            print(i)

parar(lista)
