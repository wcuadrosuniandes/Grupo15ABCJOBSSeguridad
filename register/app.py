from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
import requests
import os

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/register_candidate_information', methods=['POST'])
def register():
    return {'message': 'se registro informacion'}, 200
