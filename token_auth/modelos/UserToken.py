from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .Base import db

class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contrasena = db.Column(db.String(50))


class AdminCadenaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserToken
        include_relationships = True
        load_instance = True

    id = fields.String()