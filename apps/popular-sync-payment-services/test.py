from pydantic import BaseModel
import xml.etree.ElementTree as ET

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