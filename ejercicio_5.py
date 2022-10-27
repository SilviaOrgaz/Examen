class hash_tabla:
    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño: tamaño_tab
    def __init__(self, tamaño_tab):
        self.tamaño_tab = tamaño_tab
        self.tabla =  [None] * tamaño_tab

    def imprime_tabla(self):
        for i in range (len(self.tabla)):
            
        