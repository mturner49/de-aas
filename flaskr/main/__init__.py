from flask import Blueprint

bp = Blueprint('main', __name__)

from flaskr.main import routes