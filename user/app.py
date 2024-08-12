from flask import Flask
from routes import user_blueprint


app = Flask(__name__)

app.register_blueprint(user_blueprint)


app.run()