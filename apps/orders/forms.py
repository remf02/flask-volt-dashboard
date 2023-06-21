from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired


class OrderForm(FlaskForm):
    name_tech       = StringField("Name")
    terminal_id     = StringField("Terminal ID")
    port_id         = StringField("Port ID")
    client_longitud = StringField("Client Longitude")
    client_latitud  = StringField("Client Latitude")
    client_name     = StringField("Client Name")
    client_vat      = StringField("Client VAT")
    client_address  = StringField("Client Address")
    submit          = SubmitField("Submit")