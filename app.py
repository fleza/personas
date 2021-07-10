from flask import Flask, render_template, redirect, url_for, request
from models import *
from flask import jsonify

app = Flask(__name__)

# numero de input a mostrar
total = 10

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('layout.html', total=total)

@app.route('/api/v1/masrepetido', methods=['GET', 'POST'])
def obtener_mas_repetido():
    if request.method == 'POST':
        personas = []
        # obtener todos los nombres, entidades y municipios
        # crear objetos de tipo PersonaFisica y agregarlos a una lista para
        # utilizar la funcion obtenerMasRepetido()
        for i in range(1,total+1):
            nombre = request.form['nombre'+str(i)]
            entidad = request.form['entidad'+str(i)]
            municipio = request.form['municipio'+str(i)]
            personas.append(PersonaFisica(entidad, municipio, nombre))
    # buscar el mas repetido de la lista de personas fisicas y regresar el mas repetido 
    return obtenerMasRepetido(personas)

def obtenerMasRepetido(personas):
    counts = {}
    # contar cuantas veces aparece el nombre
    for persona in personas:
        nombre = persona.nombre.lower()
        if nombre in counts:
            counts[nombre] = counts[nombre] + 1
        else:
            counts[nombre] = 1
    # encontrar el que se repite mas
    mas_repetido = max(counts, key=lambda item: counts[item])
    mas_repetido = mas_repetido.capitalize()
    
    return jsonify(
        nombre=mas_repetido
    )

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)