import requests

from apps.orders.models import Order


class WorkerOrder(object):
    def __init__(self) -> None:
        self.session = requests.Session()

    def create_order(self):
        order = Order(
            name_tech=name_tech,
            terminal_id=terminal_id,
            port_id=port_id,
            client_longitud=client_longitud,
            client_latitud=client_latitud,
            client_name=client_name,
            client_vat=client_vat,
            client_address=client_address,
        )
        order.save()

    def run(self):
        while True:
            print("Leer continuamente desde la api")