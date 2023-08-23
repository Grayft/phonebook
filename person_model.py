from __future__ import annotations
from pydantic import BaseModel, ValidationError, field_validator
import re


class Person(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    organization_name: str
    work_phone_number: str
    mobile_phone_number: str

    @field_validator('last_name', 'middle_name', 'first_name')
    @classmethod
    def validate_name_length(cls, value):
        max_len = 25
        if len(value) > max_len or len(value) < 1:
            raise ValueError(f'Длина имени не может быть больше {max_len}')
        return value

    @field_validator('work_phone_number', 'mobile_phone_number')
    @classmethod
    def validate_mobile_phone_number(cls, value):
        valid_phone = re.fullmatch(
            r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',
            value)
        if valid_phone:
            return value
        raise ValueError('Некорректный номер телефона')

    def __eq__(self, other: Person):
        if self.last_name != other.last_name:
            return False
        if self.first_name != other.first_name:
            return False
        if self.middle_name != other.middle_name:
            return False
        return True

    def __ne__(self, other: Person):
        if (self.last_name != other.last_name or
                self.first_name != other.last_name or
                self.middle_name != other.middle_name):
            return True
        return False

    def __lt__(self, other: Person):
        if self.last_name < other.last_name:
            return True
        if (self.last_name == other.last_name and
                self.first_name < other.first_name):
            return True
        if (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.middle_name < other.middle_name):
            return True
        return False

    def __le__(self, other: Person):
        if self.last_name > other.last_name:
            return False
        if (self.last_name == other.last_name and
                self.first_name > other.first_name):
            return False
        if (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.middle_name > other.middle_name):
            return False
        return True

    def __gt__(self, other: Person):
        if self.last_name > other.last_name:
            return True
        if (self.last_name == other.last_name and
                self.first_name > other.first_name):
            return True
        if (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.middle_name > other.middle_name):
            return True
        return False

    def __ge__(self, other: Person):
        if self.last_name < other.last_name:
            return False
        if (self.last_name == other.last_name and
                self.first_name < other.first_name):
            return False
        if (self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.middle_name < other.middle_name):
            return False
        return True
