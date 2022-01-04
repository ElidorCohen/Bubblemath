from enum import Enum


class UserType (Enum):
    counselor = 1
    student = 2
    admin = 3


class Gender (Enum):
    Male = 1
    Female = 2


class User:
    def __init__(self, user_id, full_name, age,user_type, gender,institute):
        self.user_id = user_id
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.user_type = user_type
        self.institute = institute