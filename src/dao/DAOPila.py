from .DAOLinkedList import *

class Stack(LinkedList):
  """
  Implementación de una pila LIFO (Last In, First Out) utilizando una lista enlazada.
  """
  def push(self, dato):
    """
    Inserta un elemento al inicio de la pila (LIFO).
    """
    self.insertar_al_inicio(dato)

  def pop(self):
    """
    Elimina y retorna el primer elemento de la pila (LIFO).
    """
    return self.eliminar_al_inicio()
  
  def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
            
  def imprimir(self):
        """
        Devuelve una lista con todos los elementos de la pila.
        """
        return list(self)