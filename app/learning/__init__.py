from flask import Blueprint

learning = Blueprint('learning', __name__)

from app.learning import routes