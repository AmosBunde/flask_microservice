from flask import Flask
import model
from routes import user_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'aLLee3vF_ofXyZboEJy_giwpp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
model.init_app(app)

app.register_blueprint(user_blueprint)


app.run()