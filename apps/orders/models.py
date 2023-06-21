from apps import db


class Order(db.Model):
    __tablename__ = 'Orders'
    id =                db.Column(db.Integer, primary_key=True)
    name_tech =         db.Column(db.String(100))
    terminal_id =       db.Column(db.String)
    port_id =           db.Column(db.String)
    client_longitud =   db.Column(db.String)
    client_latitud =    db.Column(db.String)
    client_name =       db.Column(db.String(200))
    client_vat =        db.Column(db.String(200))
    client_address =    db.Column(db.String(255))

    def __init__(self, name_tech, terminal_id, port_id, client_longitud, client_latitud, client_name, client_vat, client_address ):
        self.name_tech = name_tech
        self.terminal_id = terminal_id
        self.port_id = port_id
        self.client_longitud = client_longitud
        self.client_latitud = client_latitud
        self.client_name = client_name
        self.client_vat = client_vat
        self.client_address = client_address

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.client_name)

    def save(self):

        # inject self into db session    
        db.session.add (self)

        # commit change and save the object
        db.session.commit()
        return self
    
    @staticmethod
    def all():
        return []
