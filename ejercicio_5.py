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
        hash = self.funcion_hash(valor)
        if self.tabla[hash] is None:
            self.tabla[hash] = valor
    #Calcula el codigo hash de cada elemento de la cadena y le sumo 33 para convertirlo a caracteres imprimibles
    #Devuelve la cadena hasheada
    def encriptar(self, cadena):
        resultado =""
        for i in cadena:
            self.Insertar_elementos(i)
            resultado = resultado + chr(self.funcion_hash(i)+33)
        return resultado
    
    #A partir de una cadena hasheada te devuelve la cadena en claro
    def des_encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            resultado = resultado + str(self.tabla[ord(i)-33])
        return resultado
    
    
alfabeto = [chr(i)for i in range(32, 125)]
#Creo la tabla hash del tamaño de la longitud del alafabeto
A= hash_tabla(len(alfabeto))

#Imprime una palabra encriptada
cadena = input("Introduce una cadena: ")
cadena_encriptada = A.encriptar(cadena)
print("Cadena encriptada: {}".format(cadena_encriptada))
cadena_des_encriptada = A.des_encriptar(cadena_encriptada)
print("Cadena desencriptado: {}".format(cadena_des_encriptada))



        