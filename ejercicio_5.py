class hash_tabla:
    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño: tamaño_tab
    def __init__(self, tamaño_tab):
        self.tamaño_tab = tamaño_tab
        self.tabla =  [None] * tamaño_tab

    def imprime_tabla(self):
        for i in range (len(self.tabla)):
            print("{}: {}".format(i, self.tabla[i]))
    
    #Calcula al funcion de una cadena.
    #Asigno un vaor de la tabla hash a cada caracter.
    #Me baso en la función de Bernstein, el numero 33 lo conocemos como el número mágico
    def funcion_hash(self, caracter):
        return ord(caracter) * 33 % self.tamaño_tab

    #Este es un método para insertar elementos
    def Insertar_elementos(self, valor):
        hash = self.function_hash(valor)
        if self.tabla[hash] is None:
            self.tabla[hash] = valor
    
    def encriptar(self, cadena):
        resultado =""
        for i in cadena:
            self.Insertar_elementos(i)
            resultado = resultado + chr(self.funcion_hash(i)+33)
        return resultado
    
    def des_encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            resultado = resultado + str(self.tabla[ord(i)])
        return resultado
    
    
alfabeto = [chr(i)for i in range(32, 125)]
A= hash_tabla(len(alfabeto))

cadena = input("Introduce una cadena: ")
cadena_encriptada = A.encriptar(cadena)
print("Cadena encriptada: {}".format(cadena_encriptada))



        