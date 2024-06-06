from flask import Flask, flash, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'mys3cretk3y'

users = {
    'jose': 'jose1',
    'jose2': 'josej2'
}

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

@app.route('/empleado/cita')
def cita():
    return render_template('/empleado/cita/index.html')

@app.route('/empleado/historial')
def historial():
    return render_template('empleado/historial/index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if  __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)