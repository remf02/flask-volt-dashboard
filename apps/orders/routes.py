# -*- encoding: utf-8 -*-
from flask import render_template, redirect, request, url_for

from apps import db, login_manager
from apps.orders import blueprint
from apps.orders.models import Order


# url/orders/
# url/orders
@blueprint.get("/")
@blueprint.get("")
def index():
    # Logica para obtener las ordenes de instalacion
    return render_template("orders/index.html", {"orders": Order.all()})


# https://urlbase/orders/1
@blueprint.get("/{id: int}")
def detail():
    # Logica para obtener el detalle de la orde segun su ID dato.
    return "detail"


# https://urlbase/orders/1
@blueprint.post("/{id: int}")
def confirm_order_installed():
    # logica para actualizar la orden segun los datos del form
    # logica para envair a la api la informas del form
    return "detail"