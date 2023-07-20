from pydantic import BaseModel, Field
import xml.etree.ElementTree as ET
from typing import Union

class DetalleModel(BaseModel):
    ID: str
    Descripcion: str
    Valor: Union[int, str]

class UserModel(BaseModel):
    CodigoMensaje: int
    DescripcionMensaje: str
    NumeroReferencia: int
    TipoReferencia: str
    IDDocumento: str
    NombreCliente: str
    MontoImpuesto: int
    MontoSaldo: int
    MontoVencido: Union[int, str] = Field(default=None)
    MontoTotal: int
    Moneda: str
    Fecha: str
    Detalles: list[DetalleModel]

    class Config:
        extra = "allow"

# Parsear el archivo XML
tree = ET.parse('data.xml')
root = tree.getroot()

# Convertir el XML en un diccionario
data = {}
for child in root:
    if child.tag == "Detalles":
        detalles = []
        for detalle in child:
            detalle_data = {
                "ID": detalle.attrib["ID"],
                "Descripcion": detalle.attrib["Descripcion"],
                "Valor": detalle.attrib["Valor"]
            }
            detalles.append(DetalleModel(**detalle_data))
        data[child.tag] = detalles
    else:
        data[child.tag] = child.text

# Validar y deserializar el diccionario utilizando Pydantic
bpd = UserModel(**data)

# Imprimir el valor de la descripción
print(bpd.DescripcionMensaje)
print(bpd.CodigoMensaje)
print(bpd.NumeroReferencia)
print(bpd.TipoReferencia)
print(bpd.IDDocumento)
print(bpd.NombreCliente)
print(bpd.MontoImpuesto)
print(bpd.MontoSaldo) 
print(bpd.MontoTotal) 
print(bpd.Moneda)
print(bpd.Fecha)
print(bpd.Detalles)
