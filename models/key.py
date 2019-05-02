
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ma
from config import db

class Key(db.Model):
    __tablename__ = 'key'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.LargeBinary, nullable=False)

class KeyScheme(ma.ModelSchema):
    class Meta:
        model = Key
        sqla_session = db.session
