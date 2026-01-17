from pydantic import BaseModel, field_validator, EmailStr, AnyUrl, Field, model_validator
# field validator works in two modes
#one is after other is before
class Pateint(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: dict[str, str]
# applying the field on email
    @field_validator('email')
    @classmethod
    def email_validator(cls, v):
        valid_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
        # extract after @
        domain_name = v.split('@')[1]
        if domain_name not in valid_domains:
            raise ValueError("Invalid domain")
        return v

    @field_validator('name')
    @classmethod
    def name_validator(cls, v):
        if len(v) < 3:
            raise ValueError("Name must be at least 3 characters long")
        return v

    @field_validator('age', mode='after')# before type version 
    @classmethod
    def age_validator(cls, v):
        if v < 0 :
            raise ValueError("Age must be greater than 0")
        return v
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is required for patients above 60 years of age")
        return model

def update_pateint_data(pateint: Pateint):
    print(pateint.name)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.allergies)
    print(pateint.contact_details)
    print(pateint.email)
    
    
    
pateint_info = {'name': "Omkar", 'email': 'omkar@gmail.com', 'age': '66', 'weight': 70.0, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': { 'phone': '9876543210', 'emergency': '9876543210'}}
pateint1 = Pateint(**pateint_info)
update_pateint_data(pateint1)