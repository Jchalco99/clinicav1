class NodoArbol:
    def __init__(self, dato):
        self.izquierda = None
        self.dato = dato
        self.derecha = None
        
class Node:
  """
  Nodo individual para la lista enlazada.
  """
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None