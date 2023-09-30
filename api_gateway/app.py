from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
import requests
import os

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

cors = CORS(app, resources={r"/*": {"origins": "*"}})

url_authenticator = os.environ.get('AUTHENTICATOR_SERVICE_URL', 'http://localhost:5001')
url_token = os.environ.get('TOKEN_AUTH_SERVICE_URL', 'http://localhost:5002')
url_register = os.environ.get('REGISTER_SERVICE_URL', 'http://localhost:5003')


@app.route('/register-candidate', methods=['POST'])
def register_candidate_information():
    data = request.get_json()
    token = request.headers.get('Authorization')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    response_token = requests.post(f'{url_token}/validate', json=data, headers=headers)
    response_code_token = response_token.status_code

    if response_code_token != 200:
        return {'error': 'Token de usuario no valido'}, 401

    response = requests.post(f'{url_register}/register_candidate_information', json=data, headers=headers)
    response_code = response.status_code

    if response_code != 200:
        return {'error': 'Error on register API'}, 500

    return {'message': 'Candidate information registered'}, 200


@app.route('/login-candidate', methods=['POST'])
def login_candidate():
    data = request.get_json()
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(f'{url_authenticator}/login', json=data, headers=headers)
    response_code = response.status_code

    if response_code != 200:
        return {'error': 'Error on login API'}, 500

    token = response.json()['token']

    return {'message': 'Candidate logged', 'token': token}, 200
