from flask import Flask, render_template

app = Flask(__name__, template_folder='Template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservas.html/')
def reservas():
    return render_template('reservas.html')

@app.route('/contacto.html/')
def contacto():
    return render_template('contacto.html')

@app.route('/iniciar_sesion.html/')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

@app.route('/registrarse.html/')
def registrarse():
    return render_template('registrarse.html')

if __name__ == '__main__':
    app.run(debug=True)