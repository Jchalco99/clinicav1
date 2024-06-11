class Cita:
    def __init__(self, id_cita=None, tipo_documento=None, numero_documento=None, datos_paciente=None, fecha_cita=None, hora_cita=None, medico=None, usuario=None, fecha_registro=None, hora_registro=None):
        self.id_cita = id_cita
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.datos_paciente = datos_paciente
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita
        self.medico = medico
        self.usuario = usuario
        self.fecha_registro = fecha_registro
        self.hora_registro = hora_registro