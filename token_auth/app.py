import hashlib
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from modelos import (
    UserToken,
    db
)
from vistas.VistaToken import VistaToken
from vistas.VistaValidateToken import VistaValidateToken

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dbapp.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "frase-secreta"
app.config["PROPAGATE_EXCEPTIONS"] = True


app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

def hash_contrasena(contrasena):
    return hashlib.md5(contrasena.encode("utf-8")).hexdigest()

sistem_contrasena = UserToken.query.first()
if not sistem_contrasena:
    sistem_token = UserToken(
        contrasena=hash_contrasena("I9f04&~RakBS")
    )
    db.session.add(sistem_token)
    db.session.commit()
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)
api.add_resource(VistaToken, "/generate")
api.add_resource(VistaValidateToken, "/validate")

jwt = JWTManager(app)


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user["user"]


@jwt.user_lookup_loader
def user_lookup_callback(_, jwt_data):
    identity = jwt_data["sub"]
    if identity != '' and identity is not None:
        return 'Acceso autorizado', 209
    else:
        return 'Unauthorized', 403
