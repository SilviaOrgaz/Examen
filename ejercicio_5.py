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


        