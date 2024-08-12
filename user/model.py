from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    is_admin = db.Columnn(db.Boolean)
    api_key  = db.Column(db.string(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<user {self.id}{self.username}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'password':self.password,
            'is_admin':self.is_admin,
            'api_key':self.api_key,
            'is_active':self.is_active
            }

