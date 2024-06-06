1. Clonar el proyecto:
git clone https://github.com/Jchalco99/clinicav1.git

2. Instalar virtualenv:
py -m pip install --user virtualenv
py -m pip install virtualenv

3. Crear el entorno virtual:
virtualenv env
py -m venv env

4. Activar el virtualenv:
env\Scripts\activate

5. Instalar flask *ACTIVADO EL ENTORNO VIRTUAL*
pip install flask

6. Si deseas desactivar en virtualenv *(OPCIONAL)*:
deactivate

7. Ejecutar el programa:
py src\app.py

8. Ejecutar el programa 2° forma:
cd src
py app.py
