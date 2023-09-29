from flask import jsonify, request
from flask_restful import Resource

from .VistaBase import candidate_required

class VistaValidateToken(Resource):   
    @candidate_required()
    def post(self):
        return {"mensaje":"Token valido"}
        


