from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ma
from config import db

class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.column(db.String)
    lastname = db.column(db.String)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)

class EmployeeSchema(ma.ModelSchema):
    class Meta:
        model = Employee
        sqla_session = db.session
