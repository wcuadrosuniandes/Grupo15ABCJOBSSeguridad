import hashlib
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from modelos import UserToken, db

from .VistaBase import candidate_required

class VistaToken(Resource):
    def post(self):
        contrasena_encriptada = hashlib.md5(
            request.json["contrasena"].encode("utf-8")
        ).hexdigest()
        sistem_contrasena = (db.session.query(UserToken).filter(
            UserToken.contrasena == contrasena_encriptada)).first()
        db.session.commit()
        if sistem_contrasena is None:
            return {"mensaje": "No autorizado"}, 403
        else:
            user =  request.json["usuario"]
            rol = request.json["rol"]
            token_de_acceso = create_access_token(
                identity={"user":user},
                additional_claims={"is_candidate": rol == 'CANDIDATE'},
            )
            return {"mensaje": "Acceso autorizado", "token": token_de_acceso}
        
    
        


