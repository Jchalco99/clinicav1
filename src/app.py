from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOCita import Cita
from dao.DAOCola import Queue
from dao.DAOPila import Stack

app = Flask(__name__)
app.secret_key = 'mys3cretk3y'

users = {
    'jose': 'jose1',
    'jose2': 'josej2'
}

cita = Cita()
cola = Queue()
pila = Stack()

# Inicio
@app.route('/')
def inicio():
    return render_template('index.html')

# Paciente
@app.route('/paciente')
def paciente():
    pacientes = ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09"]
    return render_template('/paciente/index.html', pacientes = pacientes)

# Empleado
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('empleado'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')
            return redirect(url_for('login'))
    
    return render_template('/empleado/login.html')

@app.route('/empleado')
def empleado():
    if 'username' in session:
        username = session['username']
        return render_template('/empleado/index.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/empleado/cita', methods=['GET', 'POST'])
def cita():
    if request.method == 'POST':
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        datos_paciente = request.form['datos_paciente']
        fecha_cita = request.form['fecha_cita']
        turno = request.form['turno']
        hora_cita = request.form['hora_cita']
        
        nueva_cita = Cita(tipo_documento, numero_documento, datos_paciente, fecha_cita, turno, hora_cita)
        cola.enqueue(nueva_cita)
        flash('Cita registrada exitosamente')
        return redirect(url_for('cita'))
    
    return render_template('/empleado/cita/index.html')

@app.route('/empleado/historial')
def historial():
    historial_citas = []
    nodo_actual = historial.cabeza
    while nodo_actual:
        historial_citas.append(nodo_actual.dato)
        nodo_actual = nodo_actual.siguiente
    
    return render_template('empleado/historial/index.html', historial_citas=historial_citas)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if  __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)