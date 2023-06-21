from flask import Blueprint

blueprint = Blueprint(
    'orders_blueprint',
    __name__,
    url_prefix='/orders'
)