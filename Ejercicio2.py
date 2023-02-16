#2. Crea un programa en Python que mantenga un historial de tareas pendientes. 
# El programa debe permitir al usuario agregar una tarea al inicio de la lista, 
# eliminar una tarea del final de la lista y mostrar todas las tareas en la lista en orden inverso al que se agregaron.
# Además, el programa debe contar la cantidad total de tareas en la lista y mostrar ese número al usuario.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ant = None

class ListaDoble:
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
    
    def eliminarInicio(self):
        if len(self) == 0:
            pass
        elif self.primero.sig == None:
            self.primero = self.cola = None
        else:
            self.primero = self.primero.sig
            self.primero.ant = None


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
        datos = " <<<<<<<<<<< Lista de tareas >>>>>>>>>"
        while aux != None:
            datos += str(aux.dato) + " \n "
            aux = aux.sig
        datos += "<<<<<<<<<<<<< Fin lista tareas >>>>>>>>"
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
        Opciones para hacer con la lista:
        1: Agregar tarea al Inicio
        2: Eliminar tarea al  Final
        3: Verificar si esta vacia
        4: Ver lista al revez
        5: Salir
        """)
    
        opcion = int(input("- Seleccione una opcion : "))

        if opcion == 1:
            dato = str(input("Ingrese un dato : "))
            lista.agregarInicio(dato)
        elif opcion == 2:
            lista.eliminarFinal() #Elimina el ultimo nodo
        elif opcion==3:
            if(len(lista))==0:
                print("Esta vacia")
            else:
                print("No esta vacia ")
        elif opcion==4:
            print(" Esta es la lista de datos que se estan guardando")
            print(lista)
        elif opcion ==5:
            print("Hemos salido ;-;  ")
            print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠂⢉⠤⠐⠋⠈⠡⡈⠉⠐⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⢠⣤⠔⠁⢀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠈⠱⡤⣤⠄⣀⠀⠀⠀⠀⠀
⠀⠀⠰⠁⠀⣰⣿⠃⠀⢠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢞⣦⡀⠈⡇⠀⠀⠀
⠀⠀⠀⢇⣠⡿⠁⠀⢀⡃⠀⣈⠀⠀⠀⠀⢰⡀⠀⠀⠀⠀⢢⠰⠀⠀⢺⣧⢰⠀⠀⠀⠀
⠀⠀⠀⠈⣿⠁⡘⠀⡌⡇⠀⡿⠸⠀⠀⠀⠈⡕⡄⠀⠐⡀⠈⠀⢃⠀⠀⠾⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠇⡇⠃⢠⠀⠶⡀⡇⢃⠡⡀⠀⠀⠡⠈⢂⡀⢁⠀⡁⠸⠀⡆⠘⡀⠀⠀⠀⠀
⠀⠀⠀⠸⠀⢸⠀⠘⡜⠀⣑⢴⣀⠑⠯⡂⠄⣀⣣⢀⣈⢺⡜⢣⠀⡆⡇⠀⢣⠀⠀⠀⠀
⠀⠀⠀⠇⠀⢸⠀⡗⣰⡿⡻⠿⡳⡅⠀⠀⠀⠀⠈⡵⠿⠿⡻⣷⡡⡇⡇⠀⢸⣇⠀⠀⠀
⠀⠀⢰⠀⠀⡆⡄⣧⡏⠸⢠⢲⢸⠁⠀⠀⠀⠀⠐⢙⢰⠂⢡⠘⣇⡇⠃⠀⠀⢹⡄⠀⠀
⠀⠀⠟⠀⠀⢰⢁⡇⠇⠰⣀⢁⡜⠀⠀⠀⠀⠀⠀⠘⣀⣁⠌⠀⠃⠰⠀⠀⠀⠈⠰⠀⠀
⠀⡘⠀⠀⠀⠀⢊⣤⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠄⠀⢸⠃⠀⠀⠀⠀⠀⠃⠀
⢠⠁⢀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠸⠀
⠘⠸⠘⡀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠁⠀⠃⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⢠⠀⠀⡇
⠀⠇⢆⢃⠀⠀⠀⠀⠀⡏⢲⢤⢀⡀⠀⠀⠀⠀⠀⢀⣠⠄⡚⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀
⢰⠈⢌⢎⢆⠀⠀⠀⠀⠁⣌⠆⡰⡁⠉⠉⠀⠉⠁⡱⡘⡼⠇⠀⠀⠀⠀⢀⢬⠃⢠⠀⡆
⠀⢢⠀⠑⢵⣧⡀⠀⠀⡿⠳⠂⠉⠀⠀⠀⠀⠀⠀⠀⠁⢺⡀⠀⠀⢀⢠⣮⠃⢀⠆⡰⠀
⠀⠀⠑⠄⣀⠙⡭⠢⢀⡀⠀⠁⠄⣀⣀⠀⢀⣀⣀⣀⡠⠂⢃⡀⠔⠱⡞⢁⠄⣁⠔⠁⠀
⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀
            """)
            valor = False
        else:
            print("Esa ocion no esta permitida")


ls = ListaDoble() #instanciando
lista_Opciones(ls)