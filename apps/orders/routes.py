# -*- encoding: utf-8 -*-
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required

from apps import db, login_manager
from apps.orders import blueprint
from apps.orders.models import Order
from apps.orders.forms import OrderForm
import json
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
# url/orders/
# url/orders
@blueprint.get("/")
@blueprint.get("")
@login_required
def index():
    # Logica para obtener las ordenes de instalacion
    return render_template("orders/index.html", **{"orders": []}, segment='index')


# https://urlbase/orders/1
@blueprint.route("/<int:id>", methods=["GET", "POST"])
def detail(id):
    # Logica para obtener el detalle de la orde segun su ID dato.
    form = OrderForm()
    form.terminal_id.choices = [(1, 'TE01'), (2, 'TE02')]
    form.port_id.choices = [(1, 'TE01'), (2, 'TE02')]

    if form.validate_on_submit():
        flash('Instalacion confirmada exitosamente')
        return redirect(url_for("orders_blueprint.index"))

    return render_template("orders/detail.html", **{"order_id": id, "form": form})



@blueprint.route("/api", methods=["POST"])
def api():
    if "file" not in request.files:
        flash('No se selecciono ningun archivo')
       # return "No se seleccionó ningún archivo", 400
        return redirect(url_for("orders_blueprint.orders"))

    file = request.files["file"]
    if file.filename == "":
         flash('No se selecciono ningun archivo')
       # return "No se seleccionó ningún archivo", 400
         return render_template("orders/index.html")

    if file:
        data = file.read().decode("utf-8")  # Leer el archivo y Decodicficarlo
        print("Contenido del archivo Json:")
        print(data)
        try:
            json_data = json.loads(data)  # Convertir en un Objeto Python
            return render_template("orders/index.html", data=json_data)
        except json.JSONDecodeError as e:
            print("Error al cargar el archivo JSON:", str(e))
            # Manejar el error de carga del Json Aqui

        return render_template("orders/index.html")

    return "Tipo de archivo no válido. Se requiere un archivo JSON", 400





