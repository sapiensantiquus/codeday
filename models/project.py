
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import ma
from config import db

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String)
    # customers = db.relationship(
    #     "Customer",
    #     back_populates="project")


class ProjectScheme(ma.ModelSchema):
    class Meta:
        model = Project
        sqla_session = db.session
