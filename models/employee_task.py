from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ma
from config import db

class EmployeeTask(db.Model):
    __tablename__ = 'employee_task'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.Integer, nullable=False)
    starttime = db.Column(db.DateTime)
    endtime = db.Column(db.DateTime)

class EmployeeTaskSchema(ma.ModelSchema):
    class Meta:
        model = EmployeeTask
        sqla_session = db.session
