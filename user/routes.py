from flask import Blueprint

user_blueprint = Blueprint('user_api_routes',__name__,url_prefix='/api/user')

@user_blueprint.route('/')

def index():
    return "Hello World"