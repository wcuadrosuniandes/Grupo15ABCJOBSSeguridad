from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
import requests
import os

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

cors = CORS(app, resources={r"/*": {"origins": "*"}})

host = os.environ.get('HOST', 'localhost')
port = os.environ.get('PORT', '5002')
url = f'http://{host}:{port}'

user_allowed = {
    'usuario': 'admin',
    'contrasena': 'I9f04&~RakBS'
}


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if data['usuario'] != user_allowed['usuario'] or data['contrasena'] != user_allowed['contrasena']:
        return {'error': 'Error on login API'}, 401


    reponse = requests.post(f'{url}/generate', json=data)
    response_code = reponse.status_code

    if response_code != 200:
        return {'error': 'Error on login API'}, 500

    token = reponse.json()['token']

    return {'message': 'User autenticated', 'token': token}, 200
