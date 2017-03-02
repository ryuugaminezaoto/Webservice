from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

Webservice = [{
    'nombre': u'temperatura',
    'url': u'http://www.watoto.mx/temperatura/mes=enero'
},
    {
        'nombre': u'pulso',
        'url': u'http://www.watoto.mx/pulso'
    }
]

@app.route('/Webservice', methods=['GET'])
def get_tasks():
    return jsonify({'Webservice': Webservice})

@app.route('/Webservice/<string:nombre>', methods = ['GET'])
def get_task(nombre):
    servicio = [servicio for servicio in Webservice if servicio['nombre'] == nombre]
    if len(servicio) == 0:
        abort(404)
    return jsonify({'Webservice': servicio[0]})
@app.errorhandler(404)
def no_encontrado(error):
    return make_response(jsonify({'404':'No Encontrado'}), 400)

if __name__ == '__main__':
    app.run(debug=True)
