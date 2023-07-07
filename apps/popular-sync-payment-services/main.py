import datetime
import time
from typing import List, Optional
from pydantic import BaseModel


class Payment():
    pass

class PopularSyncPayment:
    seconds = 5000  #.env 

    def __int__(self):
       # self.odoo_services = OdooService()
        pass

        def run(self):
            pass

        def send_payment_to_odoo(self, data):
            pass

        def read_xml(self):
            pass
            #Testing XML para procesar la informacion enviada al BPD

            def xml_to_pay(self):
                pass


class UserModel(BaseModel):
    name: str
    age: int
    email: str


# Analizar el archivo XML
tree = ET.parse('data.xml')
root = tree.getroot()

# Convertir el XML en un diccionario
data = {}
for child in root:
    data[child.tag] = child.text

# Validar y deserializar el diccionario utilizando Pydantic
user = UserModel(**data)
print(user.age)    


def main():
    sync = PopularSyncPayment()
    sync.run()

#if__name__=="__main__":
