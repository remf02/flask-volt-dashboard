# -*- encoding: utf-8 -*-
from flask import render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user

from flask_dance.contrib.github import github

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users
import json

from apps.authentication.util import verify_pass


@blueprint.route("/")
def route_default():
    return redirect(url_for("authentication_blueprint.login"))


# Login & Registration


@blueprint.route("/github")
def login_github():
    """Github login"""
    if not github.authorized:
        return redirect(url_for("github.login"))

    res = github.get("/user")
    return redirect(url_for("home_blueprint.index"))


# @blueprint.route("/orders", methods=["GET", "POST"])
# def orders():
#     form = OrderForm()
#     msg = None
#     success = False

#     if request.method == "POST" and form.validate:
#         name_tech = request.form.get("name_tech", "", type=str)
#         terminal_id = request.form.get("terminal_id", "", type=str)
#         port_id = request.form.get("port_id", "", type=str)
#         client_longitud = request.form.get("client_longitud", "", type=str)
#         client_latitud = request.form.get("client_latitud", "", type=str)
#         client_name = request.form.get("client_name", "", type=str)
#         client_address = request.form.get("client_address", "", type=str)
#         client_vat = request.form.get("client_vat", "", type=str)

#         print("name_tech:", name_tech)
#         print("terminal_id:", terminal_id)
#         print("port_id:", port_id)
#         print("client_longitud:", client_longitud)
#         print("client_latitud:", client_latitud)
#         print("client_name:", client_name)
#         print("client_vat:", client_vat)
#         print("client_address", client_address)
#         # Resto del código...

#         order = Order(
#             name_tech=name_tech,
#             terminal_id=terminal_id,
#             port_id=port_id,
#             client_longitud=client_longitud,
#             client_latitud=client_latitud,
#             client_name=client_name,
#             client_vat=client_vat,
#             client_address=client_address,
#         )

#         order.save()
#         msg = "Registro guardado exitosamente"
#         success = True

#     return render_template("orders.html", form=form, msg=msg, success=success)





@blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    if "login" in request.form:
        # read form data
        username = request.form["username"]
        password = request.form["password"]

        # Locate user
        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for("authentication_blueprint.route_default"))

        # Something (user or pass) is not ok
        return render_template(
            "accounts/login.html", msg="Wrong user or password", form=login_form
        )

    if not current_user.is_authenticated:
        return render_template("accounts/login.html", form=login_form)
    return redirect(url_for("home_blueprint.index"))


@blueprint.route("/register", methods=["GET", "POST"])
def register():
    create_account_form = CreateAccountForm(request.form)
    if "register" in request.form:
        username = request.form["username"]
        email = request.form["email"]

        # Check usename exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template(
                "accounts/register.html",
                msg="Username already registered",
                success=False,
                form=create_account_form,
            )

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template(
                "accounts/register.html",
                msg="Email already registered",
                success=False,
                form=create_account_form,
            )

        # else we can create the user
        user = Users(**request.form)
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()

        return render_template(
            "accounts/register.html",
            msg="Account created successfully.",
            success=True,
            form=create_account_form,
        )

    else:
        return render_template("accounts/register.html", form=create_account_form)


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("authentication_blueprint.login"))


# Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("home/page-403.html"), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template("home/page-403.html"), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template("home/page-404.html"), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template("home/page-500.html"), 500
