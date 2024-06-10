'''
Tipo de documento
Numero de documento
Datos del paciente
Fecha de la cita
Turno
Hora de la cita
'''

class Cita:
    def __init__(self, tipo_documento=None, numero_documento=None, datos_paciente=None, fecha_cita=None, turno=None, hora_cita=None):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.datos_paciente = datos_paciente
        self.fecha_cita = fecha_cita
        self.turno = turno
        self.hora_cita = hora_cita

    def __str__(self):
        return (f"Cita:\n"
                f"  Tipo de documento: {self.tipo_documento}\n"
                f"  Número de documento: {self.numero_documento}\n"
                f"  Datos del paciente: {self.datos_paciente}\n"
                f"  Fecha de la cita: {self.fecha_cita}\n"
                f"  Turno: {self.turno}\n"
                f"  Hora de la cita: {self.hora_cita}\n")
