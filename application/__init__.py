
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
app.config['SECRET_KEY'] = '162f2b765021ccb753815b0f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from application import routes