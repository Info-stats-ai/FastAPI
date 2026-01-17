from pydantic import BaseModel
import yaml
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

address = Address(**address_dict)

patient_dict = {'name': 'Omkar', 'age': 26, 'height': 1.71, 'address': address_dict}
patient1= Patient(**patient_dict)
print(patient1)


# model_dump is used to convert the model to a dictionary
patient_dict = patient1.model_dump()
print(patient_dict)

# model_dump_json is used to convert the model to a json string
patient_json = patient1.model_dump_json()
print(patient_json)

# model_dump_yaml is used to convert the model to a yaml string
patient_yaml = yaml.dump(patient1.model_dump())
print(patient_yaml)
