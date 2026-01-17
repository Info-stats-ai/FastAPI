from pydantic import BaseModel
class Address(BaseModel):
    house_no: str
    street_no: str
    city: str
    state: str
    country: str
class Patient(BaseModel):
    name: str
    age: int
    height: float
    address: Address

address_dict = {'house_no': '7', 'street_no': '10', 'city': 'Mumbai', 'state': 'Maharashtra', 'country': 'India'}

pateint_dict = {'name': 'Omkar', 'age': 26, 'height': 1.71, 'address': address_dict}
pateint1 = Patient(**pateint_dict)
print(pateint1)

