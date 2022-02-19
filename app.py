from flask import Flask, jsonify
from data import *

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    return jsonify(instrucciones, rutas['rutas'])

@app.route('/<string:area>')
def areas(area):
    dato_buscado = [dato for dato in invap if dato['_id'] == area]
    dato_erroneo = 'La ruta '/{}' no existe.'.format(area)
    rutas_validas = 'Las rutas válidas son: {}'.format(rutas['rutas'])
    if len(dato_buscado) > 0:
        return jsonify(dato_buscado[0])
    return jsonify(dato_erroneo, rutas_validas)

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    print(' * API INVAP')
    app.run(debug=True)
