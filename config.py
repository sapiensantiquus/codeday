import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db_user = os.environ['PG_USER']
db_pass = os.environ['PG_PASS']

basedir = os.path.abspath(os.path.dirname(__file__))


options = {"swagger_ui": True}
app = connexion.App(__name__, specification_dir=basedir + "/swagger")
#app = connexion.App(__name__, port=9090, options=options, specification_dir='swagger/')
app.app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.app.config['SQLALCHEMY_ECHO'] = True
app.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{}:{}@localhost/covermymeds".format(db_user,db_pass)
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance

db = SQLAlchemy(app.app)


# Initialize Marshmallow

ma = Marshmallow(app.app)
