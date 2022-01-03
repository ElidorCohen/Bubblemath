from enum import Enum


class UserType (Enum):
    counselor = 1
    student = 2
    admin = 3


class Gender (Enum):
    Male = 1
    Female = 2


class User:
    def __init__(self, user_id, first_name, last_name, age,user_type, gender):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.user_type = user_type
        self.gender = gender
        self.user_type = user_type