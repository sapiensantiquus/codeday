from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ma
from config import db

class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    description = db.Column(db.String, nullable=False)

class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
        sqla_session = db.session
