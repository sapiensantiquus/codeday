
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ma
from config import db

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
#    projects = db.relationship("project")

class CustomerScheme(ma.ModelSchema):
    class Meta:
        model = Customer
        sqla_session = db.session
