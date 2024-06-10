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
