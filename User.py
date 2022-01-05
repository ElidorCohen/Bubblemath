from enum import Enum


class UserType (Enum):
    counselor = 1
    student = 2
    admin = 3


class Gender (Enum):
    Male = 1
    Female = 2


class User:
    def __init__(self, user_id, full_name, age,user_type, gender,institute,score = 0,right_ans = 0,wrong_ans = 0):
        self.user_id = user_id
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.user_type = user_type
        self.institute = institute
        self.score = score
        self.right_ans = right_ans
        self.wrong_ans = wrong_ans