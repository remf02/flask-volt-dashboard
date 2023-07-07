from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import Email, DataRequired


class OrderForm(FlaskForm):
    name_tech       = StringField("Name")
    terminal_id     = SelectField("Terminal", validators=[DataRequired()])
    port_id         = SelectField("Puerto", validators=[DataRequired()])
    client_longitud = StringField("Client Longitude")
    client_latitud  = StringField("Client Latitude")
    client_name     = StringField("Client Name")
    client_vat      = StringField("Client VAT")
    client_address  = StringField("Client Address")
    submit          = SubmitField("Submit")


class PaymentForm(FlaskForm):
    pass
    


