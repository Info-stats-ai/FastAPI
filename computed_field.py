from pydantic import BaseModel, computed_field

class Pateint(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

def update_pateint_data(pateint: Pateint):
        print(pateint.name)
        print(pateint.age)
        print(pateint.height)
        print(pateint.weight)
        print(pateint.married)
        print(pateint.allergies)
        print(pateint.contact_details)
        print(pateint.bmi)
  

pateint_info = {'name': "Omkar", 'age': 26, 'height': 1.71, 'weight': 70.0, 'married': False, 'allergies': ['pollen', 'dust'], 'contact_details': { 'phone': '9876543210'}}
pateint1 = Pateint(**pateint_info)

update_pateint_data(pateint1)
