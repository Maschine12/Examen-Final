class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ant = None

class Lista:
    def __init__(self):
        self.primero = None
        self.cola = None
    
    def agregarInicio(self, dato):
        nodo = Nodo(dato)
        if len(self) == 0:
            self.primero = self.cola = nodo
        else:
            aux = nodo
            aux.sig = self.primero
            self.primero.ant = aux
            self.primero = aux

    def agregarFinal(self, dato):
        nodo = Nodo(dato)
        if len(self) == 0:
            self.primero = self.cola = nodo
        else:
            aux = self.cola
            self.cola = aux.sig = nodo
            self.cola.ant = aux
    
    def eliminarFinal(self):
        if len(self) == 0:
            pass
        elif self.primero.sig == None:
            self.primero = self.cola
        else:
            self.cola = self.cola.ant
            self.cola.sig = None
    
    def buscarNodo(self, dato):
        existe = False
        aux = self.primero
        while aux != None:
            if aux.dato == dato:
                existe = True
                break
            aux = aux.sig
        return existe
    
    def reemplazarNodo(self, anterior, nuevoDato):
        if self.buscarNodo(anterior):
            aux = self.primero
            while aux != None:
                if aux.dato == anterior:
                    aux.dato = nuevoDato
                    break
                aux = aux.sig
    
    def eliminarNodo(self, dato):
        if self.buscarNodo(dato):
            actual = self.primero
            anterior = self.primero

            while actual:
                if actual.dato == dato:
                    if actual == self.primero:
                        self.primero = actual.sig
                    else:
                        anterior.sig = actual.sig
                    return
                anterior = actual
                actual = actual.sig
        else:
            raise Exception ("El Nodo no puede se eliminado por tratarse de un dato inexistente.")
    def __len__(self):
        aux = self.primero
        count = 0
        while aux != None:
            count += 1
            aux = aux.sig
        return count
    
    def recorrer_inicio(self):
        aux = self.primero

        while aux != None:
            print(aux.dato)
            aux = aux.sig
    
    def recorrer_final(self):
        aux = self.cola
        while aux != None:
            print(aux.dato)
            aux = aux.ant
    
    def __str__(self) -> str:
        aux = self.primero
        datos = " <:"
        while aux != None:
            datos += str(aux.dato) + " : "
            aux = aux.sig
        datos += ">"
        return datos
    
    def __getitem__(self, indice):
        if indice >= 0 and indice < len(self):
            actual = self.primero
            for i in range(indice):
                actual = actual.sig

            return actual.dato
        elif indice <= -1 and indice >= -len(self):
            actual = self.cola

            for i in range(indice*(-1)-1):
                actual = actual.ant
            return actual.dato
        else:
            raise IndexError ("Indice fuera de rango")

def lista_Opciones(lista):
    valor = True
    while valor :
        print("""
        Opciones para hacer con la lista compras:
        1: Agregar elemento al Inicio
        2: Agregar elemento al Final
        3: Eliminar elemento Inicio
        4: Eliminar elemento Final
        5: Verificar si esta vacia
        6: Ver lista
        7: Salir
        """)
    
        opcion = int(input("- Seleccione una opcion : "))

        if opcion == 1:
            dato = int(input("Ingrese un dato : "))
            lista.agregarInicio(dato)
        elif opcion == 2:
            dato = int(input("Ingrese un dato : "))
            lista.agregarFinal(dato)
        elif opcion == 3:
            lista.eliminarInicio() #elimina el primer nodo
        elif opcion == 4:
            lista.eliminarFinal() #Elimina el ultimo nodo
        elif opcion==5:
            if(len(lista))==0:
                print("Esta vacia")
            else:
                print("No esta vacia ")
        elif opcion==6:
            print(" Esta es la lista de datos que se estan guardando")
            print(lista)
        elif opcion ==7:
            print("Hemos salido ;-;  ")
            valor = False
        else:
            print("Esa ocion no esta permitida")


ls = Lista() #instanciando
lista_Opciones(ls)