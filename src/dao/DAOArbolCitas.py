from .DAONode import *
from .DAOLinkedList import *
class ArbolCitas:
    def __init__(self):
        self.raiz = None

    def insertar(self, cita):
        if self.raiz is None:
            self.raiz = NodoArbol(cita)
        else:
            if self._buscar_cita_existente(self.raiz, cita):
                print("Ya existe una cita para este médico en la misma fecha y hora.")
            else:
                self._insertar_recursivo(self.raiz, cita)

    def _insertar_recursivo(self, actual, cita):
        if cita.fecha_cita < actual.dato.fecha_cita or (cita.fecha_cita == actual.dato.fecha_cita and cita.hora_cita < actual.dato.hora_cita):
            if actual.izquierda is None:
                actual.izquierda = NodoArbol(cita)
            else:
                self._insertar_recursivo(actual.izquierda, cita)
        else:
            if actual.derecha is None:
                actual.derecha = NodoArbol(cita)
            else:
                self._insertar_recursivo(actual.derecha, cita)

    def _buscar_cita_existente(self, nodo, cita):
        if nodo:
            if cita.fecha_cita == nodo.dato.fecha_cita and cita.hora_cita == nodo.dato.hora_cita and cita.medico == nodo.dato.medico:
                return True
            return self._buscar_cita_existente(nodo.izquierda, cita) or self._buscar_cita_existente(nodo.derecha, cita)
        return False

    def eliminar(self, id_cita):
        self.raiz = self._eliminar_recursivo(self.raiz, id_cita)

    def _eliminar_recursivo(self, nodo, id_cita):
        if nodo is None:
            return nodo

        if id_cita < nodo.dato.id_cita:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, id_cita)
        elif id_cita > nodo.dato.id_cita:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, id_cita)
        else:
            # Caso 1: El nodo es una hoja
            if nodo.izquierda is None and nodo.derecha is None:
                nodo = None
            # Caso 2: El nodo tiene un hijo
            elif nodo.izquierda is None:
                nodo = nodo.derecha
            elif nodo.derecha is None:
                nodo = nodo.izquierda
            # Caso 3: El nodo tiene dos hijos
            else:
                temp = self._min_valor_nodo(nodo.derecha)
                nodo.dato = temp.dato
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.dato.id_cita)

        return nodo

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def mostrar_por_dni(self, numero_documento):
        return self._buscar_por_dni(self.raiz, numero_documento)

    def _buscar_por_dni(self, nodo, numero_documento):
        if nodo is None:
            return None
        if nodo.dato.numero_documento == numero_documento:
            return nodo.dato
        izquierda = self._buscar_por_dni(nodo.izquierda, numero_documento)
        if izquierda is not None:
            return izquierda
        return self._buscar_por_dni(nodo.derecha, numero_documento)

    def ordenar_citas(self):
        lista_enlazada = LinkedList()  # Crear una lista enlazada
        self._inorden_lista(self.raiz, lista_enlazada)  # Llenar la lista enlazada
        return lista_enlazada

    def _inorden_lista(self, nodo, lista_enlazada):
        if nodo:
            self._inorden_lista(nodo.izquierda, lista_enlazada)
            lista_enlazada.insertar_al_final(nodo.dato)  # Insertar en la lista enlazada
            self._inorden_lista(nodo.derecha, lista_enlazada)
