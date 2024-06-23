from flask import Flask, flash, render_template, redirect, url_for, request, session
import jsonify
from dao.DAOCita import Cita
from dao.DAOCola import Queue
from dao.DAOPila import Stack
from dao.DAOArbolCitas import ArbolCitas
from dao.funtions import generar_id_cita, verificar_cita_existente, imprimir_por_numero_documento

app = Flask(__name__)
app.secret_key = 'mys3cretk3y'

users = {
    'jose': 'jose1',
    'jose2': 'josej2'
}

cita = Cita()
pacienteCola = Queue()
cola = Queue()
pila = Stack()
pilaDni = Stack()
arbolCitas = ArbolCitas()

# Inicio
@app.route('/')
def inicio():
    return render_template('index.html')

# Paciente
@app.route('/paciente')
def paciente():
    nuevo_paciente = f'A{len(pacienteCola) + 1:02d}'
    pacienteCola.enqueue(nuevo_paciente)
    return redirect(url_for('ver_pacientes'))

@app.route('/ver_pacientes')
def ver_pacientes():
    pacientes = list(pacienteCola)
    return render_template('paciente/index.html', pacientes=pacientes)

@app.route('/agregar_paciente', methods=['POST'])
def agregar_paciente():
    nuevo_paciente = f'A{len(pacienteCola) + 1:02d}'
    pacienteCola.enqueue(nuevo_paciente)
    pacientes = list(pacienteCola)
    return jsonify(pacientes=pacientes)

@app.route('/eliminar_paciente')
def eliminar_paciente():
    pacienteCola.dequeue()
    return redirect(url_for('ver_pacientes'))

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
        try:
            tipo_documento = request.form['tipo_documento']
            numero_documento = request.form['numero_documento']
            datos_paciente = request.form['datos_paciente']
            fecha_cita = request.form['fecha_cita']
            hora_cita = request.form['hora_cita']
            consultorio = request.form['consultorio']
            id_cita = generar_id_cita(fecha_cita, hora_cita, consultorio)

            nueva_cita = Cita(id_cita, tipo_documento, numero_documento, datos_paciente, fecha_cita, hora_cita, consultorio)
            X = arbolCitas.insertar(nueva_cita)
            pila.push(nueva_cita)
            if X == False:
                pila.pop()
                flash('La cita no se registró')
            else:
                pacienteCola.dequeue()
                flash('Cita registrada exitosamente')

            return redirect(url_for('cita'))
        
        except KeyError as e:
            flash(f"Error en los datos del formulario: campo {str(e)} faltante.")
        except ValueError as e:
            flash(f"Error en los datos del formulario: {str(e)}")
        except Exception as e:
            flash(f"Ocurrió un error al registrar la cita: {str(e)}")
    
    return render_template('/empleado/cita/index.html')

@app.route('/buscar_consultorio', methods=["POST"])
def buscar_cita():
    fecha_cita = request.form['fecha_cita2']
    turno = request.form['turno2']
    hora_cita = request.form['hora_cita2']
    consultorio = request.form['consultorio2']

    existe = verificar_cita_existente(arbolCitas, fecha_cita, hora_cita, consultorio)
    
    if existe:
        flash('No hay horario disponible')
        return redirect(url_for('cita'))
    else:
        flash('Si hay horario disponible')
        return render_template('/empleado/cita/index.html', existe=existe, fecha_cita=fecha_cita,turno=turno, hora_cita=hora_cita, consultorio=consultorio)

@app.route('/empleado/historial')
def historial():
    historial_citas = pila.imprimir()
    return render_template('empleado/historial/index.html', historial_citas=historial_citas)

@app.route('/empleado/dni')
def dni():
    return render_template('/empleado/historial/dni.html')

@app.route('/busqueda_dni', methods=["POST"])
def busqueda_dni():
    tipo_documento = request.form['tipo_documento']
    numero_documento = request.form['numero_documento']

    cita_dni = imprimir_por_numero_documento(pila, tipo_documento, numero_documento)
    dni = cita_dni.imprimir()
    return render_template('/empleado/historial/dni.html', dni=dni)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if  __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)