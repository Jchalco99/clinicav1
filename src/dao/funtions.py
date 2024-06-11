from .DAOCita import Cita

def generar_id_cita(tipo_documento, numero_documento, datos_paciente, fecha_cita, hora_cita): #, numero_doctor, usuario, fecha_registro, hora_registro):
    # Formatear la fecha y la hora
    fecha_formateada = fecha_cita.replace("-", "")
    hora_formateada = hora_cita.replace(":", "")
    
    # Concatenar la fecha, la hora y el número de doctor
    id_cita = fecha_formateada + hora_formateada # + str(numero_doctor)

    # Crear el objeto cita con el ID generado y los demás datos proporcionados
    cita = Cita(id_cita, tipo_documento, numero_documento, datos_paciente, fecha_cita, hora_cita) #, numero_doctor, usuario, fecha_registro, hora_registro)

    return cita


