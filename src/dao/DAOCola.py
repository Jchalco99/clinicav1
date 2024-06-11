from .DAOLinkedList import *

class Queue(LinkedList):
  """
  Implementación de una cola FIFO (First In, First Out) utilizando una lista enlazada.
  """
  def enqueue(self, dato):
    """
    Inserta un elemento al final de la cola (FIFO).
    """
    self.insertar_al_final(dato)

  def dequeue(self):
    """
    Elimina y retorna el primer elemento de la cola (FIFO).
    """
    return self.eliminar_al_inicio()
  
  def __len__(self):
        """
        Retorna la cantidad de datos que existe en la cola
        """
        return self.length()
  
  def __iter__(self):
        """
        Retorna un iterador para la cola.
        """
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
  
  def length(self):
        """
        Retorna el número de elementos en la lista.
        """
        nodo_actual = self.cabeza
        count = 0
        while nodo_actual is not None:
            count += 1
            nodo_actual = nodo_actual.siguiente
        return count
