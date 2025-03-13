from flask import Blueprint

markets_bp = Blueprint('markets', __name__)

from . import routes