from re import L
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class Pateint(BaseModel):
    name: Annotated[str, Field(min_length= 3, max_length= 50, title="Name of the pateint", description="Name of the pateint should be between 3 and 50 characters")]# ... means required and min_length means minimum length and max_length means maximum length
    email: EmailStr
    linkedin: AnyUrl
    age: Annotated[int, Field(gt= 0, lt= 100)]# ... means required and ge means greater than and le means less than
    weight: Annotated[float, Field(gt= 0, strict= True)] # stric type checking means if the value is not a float it will raise an error# 
    married: Optional[bool] = None # if it is not given by the user
    allergies: List[str]  = Field(min_items= 1, max_items= 10)# list must be type string 
    contact_details: Dict[str, str] # key and value must str
    
    

#def insert_pateint_data(name: str, age: int):

    #print(name, age)

#insert_pateint_data("Ananya", 'thirty')
# it will work but it should not because of the type error 
# age should be inthe format of of integer not string
# pydantic is written in rust


def insert_pateint_data(pateint: Pateint):

    print(pateint.name)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact_details)
    print(pateint.email)


pateint_info = {'name': "Omkar",'email': 'omkar@gmail.com', 'age': 26, 'weight': 70.0, 'linkedin': 'https://www.linkedin.com/in/omkar-kale/', 'allergies': ['pollen', 'dust'], 'contact_details': { 'phone': '9876543210'}}
pateint1 = Pateint(**pateint_info)
print(pateint1)
insert_pateint_data(pateint1)