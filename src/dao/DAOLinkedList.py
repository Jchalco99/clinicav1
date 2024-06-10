class Node:
  """
  Nodo individual para la lista enlazada.
  """
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

class LinkedList:
    """
    Implementación de una lista enlazada simple.
    """
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        """
        Inserta un elemento al inicio de la lista enlazada.
        """
        nuevo_nodo = Node(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        """
        Inserta un elemento al final de la lista enlazada.
        """
        if self.cabeza is None:
            self.insertar_al_inicio(dato)
            return

        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente

        nuevo_nodo = Node(dato)
        nodo_actual.siguiente = nuevo_nodo

    def eliminar_al_inicio(self):
        """
        Elimina el primer elemento de la lista enlazada.
        """
        if self.cabeza is None:
            raise Exception("La lista está vacía")

        dato_eliminado = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        return dato_eliminado

    def eliminar_al_final(self):
        """
        Elimina el último elemento de la lista enlazada.
        """
        if self.cabeza is None:
            raise Exception("La lista está vacía")

        if self.cabeza.siguiente is None:
            dato_eliminado = self.cabeza.dato
            self.cabeza = None
            return dato_eliminado

        nodo_anterior = self.cabeza
        nodo_actual = self.cabeza.siguiente
        while nodo_actual.siguiente is not None:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        dato_eliminado = nodo_actual.dato
        nodo_anterior.siguiente = None
        return dato_eliminado

    def buscar(self, dato):
        """
        Busca un elemento en la lista enlazada.
        """
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.dato == dato:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def imprimir(self):
        """
        Imprime los elementos de la lista enlazada.
        """
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato, end=" ")
            nodo_actual = nodo_actual.siguiente
        print()