from pydantic import BaseModel, ValidationError, field_validator
from base_model import Model


class Person(BaseModel):
    last_name: str
    middle_name: str
    first_name: str
    organization_name: str
    work_phone_number: str
    mobile_phone_number: str

    @field_validator('last_name', 'middle_name', 'first_name')
    @classmethod
    def validate_name_length(cls, value):
        raise NotImplementedError('Data class validator must be implemented!')

    @field_validator('mobile_phone_number')
    @classmethod
    def validate_mobile_phone_number(cls, value):
        raise NotImplementedError('Data class validator must be implemented!')


class PersonModel(Model):
    pass

if __name__ == '__main__':
    # person_model = Model(Person, 'my_datajson')
    # person_model.objects.all().
    pass

