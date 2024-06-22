from .DAOCita import Cita

def generar_id_cita(fecha_cita, hora_cita, numero_consultorio): #, usuario, fecha_registro, hora_registro):
    # Formatear la fecha y la hora
    fecha_formateada = fecha_cita.replace("-", "")
    hora_formateada = hora_cita.replace(":", "")
    
    # Concatenar la fecha, la hora y el número de doctor
    id_cita = fecha_formateada + hora_formateada + str(numero_consultorio)

    # Crear el objeto cita con el ID generado y los demás datos proporcionados
    return id_cita

def asignar_consultorio(arbol, fecha, hora):
    consultorio = 1
    while consultorio <= 4:
        if not verificar_cita_existente(arbol, fecha, hora, consultorio):
            return consultorio
        consultorio += 1
    return consultorio-1

def verificar_cita_existente(arbol, fecha, hora, consultorio):
    def _buscar_cita(nodo):
        if nodo is None:
            return True
        if nodo.dato.fecha_cita == fecha and nodo.dato.hora_cita == hora and nodo.dato.consultorio == consultorio:
            return False
        return _buscar_cita(nodo.izquierda) or _buscar_cita(nodo.derecha)

    return _buscar_cita(arbol.raiz)
