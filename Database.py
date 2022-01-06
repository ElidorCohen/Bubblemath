import pymongo
from pymongo import MongoClient
from pymongo import database
from typing import List

from User import User, UserType
from Institute import Institute
from Message import Message,Feedback

DATABASE = "BubbleMath"
ADMIN = "admin"
ADMIN_PASS = "GF7JmQYsRagdDIeu"
USERS_COLLECTION = "Users"
INSTITUTE_COLLECTION = "Institutes"
REPORTS_COLLECTION = "Reports"
GENERAL_COLLECTION = "General"
MESSAGES_COLLECTION = "Messages"
FEEDBACKS_COLLECTION = "Feedbacks"

# Commands
CREATE_USER = "createUser"


class Report():
    def __init__(self,text):
        self.text = text

class Database:
    host = "mongodb+srv://{}:{}@cluster0.r0eft.mongodb.net/{}?retryWrites=true&w=majority".format(ADMIN, ADMIN_PASS, DATABASE)
    client = MongoClient()
    is_connected = False
    is_connecting = False
    is_logged_in = False
    is_logging_in = False
    user_type = None
    user_id = None

    @staticmethod
    def connectToServer():
        if Database.is_connecting:
            return
        if Database.is_connected:
            return False
        try:
            Database.is_connecting = True
            Database.client = pymongo.MongoClient(Database.host)
            Database.is_connected = True
            print("Connected")
            return True
        except pymongo.errors.ServerSelectionTimeoutError as err:
            Database.is_connecting = False
            return False

    @staticmethod
    def getReports():
        list = []
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            reports = db.get_collection(REPORTS_COLLECTION)
            data = reports.find()
            for item in data:
                list.append(item["text"])
        return list
    
    @staticmethod
    def sendReport(text):
        report = Report(text)     
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            reports = db.get_collection(REPORTS_COLLECTION)
            data = {"text": report.text}
            reports.insert_one(data)

    @staticmethod
    def send_feedback(to_user_id,text,grade):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(FEEDBACKS_COLLECTION)
            data = {"from_user_id": Database.user_id,
                    "to_user_id": to_user_id,
                    "text": text,
                    "grade": grade}
            col.insert_one(data)

    @staticmethod
    def get_feedbacks() -> List[Feedback]:
        feed_list = []
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(FEEDBACKS_COLLECTION)
            data = col.find({"to_user_id": Database.user_id})
            if data is not None:
                for i in data:
                    msg = Feedback(i["from_user_id"], i["to_user_id"], i["text"],i["grade"])
                    feed_list.append(msg)
                return feed_list
        return None

    @staticmethod
    def send_message(to_user_id,text):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(MESSAGES_COLLECTION)
            data = {"from_user_id": Database.user_id,
                    "to_user_id": to_user_id,
                    "text": text}
            col.insert_one(data)

    @staticmethod
    def get_messages() -> List[Message]:
        msg_list = []
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(MESSAGES_COLLECTION)
            data = col.find({"to_user_id": Database.user_id})
            if data is not None:
                for i in data:
                    msg = Message(i["from_user_id"], i["to_user_id"], i["text"])
                    msg_list.append(msg)
                return msg_list
        return None

    @staticmethod
    def get_all_users() -> List[User]:
        user_list = []
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(USERS_COLLECTION)
            data = col.find()
            if data is not None:
                for i in data:
                    user = User(i["_id"],
                                i["full_name"],
                                i["age"],
                                i["user_type"],
                                i["gender"],
                                i["institute_id"],
                                i["score"],
                                i["right_ans"],
                                i["num_of_questions"])
                    user_list.append(user)
                return user_list
        return None

    @staticmethod
    def getUser(user_id):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            users = db.get_collection(USERS_COLLECTION)
            data = users.find_one({"_id": user_id})
            if data is not None:
                user = User(data["_id"],
                            data["full_name"],
                            data["age"],
                            data["user_type"],
                            data["gender"],
                            data["institute_id"],
                            data["score"],
                            data["right_ans"],
                            data["num_of_questions"])
                return user
            return None
    
    @staticmethod
    def set_admin_msg(text):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(GENERAL_COLLECTION)
            data = col.find_one({"_id": "admin_msg"})
            update = {
                    "$set": {
                        "text": text,
                    }
                    }
            col.find_one_and_update(data,update)


    @staticmethod
    def get_admin_msg():
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(GENERAL_COLLECTION)
            data = col.find_one({"_id": "user_id"})
            return data["text"]
        return None

    @staticmethod
    def set_update_available(is_available):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(GENERAL_COLLECTION)
            data = col.find_one({"_id": "update"})
            update = {
                "$set": {
                    "is_available": is_available,
                }
            }
            col.find_one_and_update(data, update)

    @staticmethod
    def get_available_update_link():
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(GENERAL_COLLECTION)
            data = col.find_one({"_id": "update"})
            if data["is_available"]:
                return data["link"]
        return None

    @staticmethod
    def set_time_per_question(time):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(GENERAL_COLLECTION)
            data = col.find_one({"_id": "game_settings"})
            update = {
                "$set": {
                    "time_per_question": time,
                }
            }
            col.find_one_and_update(data, update)

    @staticmethod
    def get_time_per_question():
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            col = db.get_collection(GENERAL_COLLECTION)
            data = col.find_one({"_id": "game_settings"})
            return int(data["time_per_question"])
        return None

    @staticmethod
    def register(user_id, first_name, password, gender, institute_id, age, user_type):
        if Database.is_connected:
            try:
                db = Database.client.get_database(DATABASE)
                users = db.get_collection(USERS_COLLECTION)
                user_data = {"_id": user_id,
                             "pwd": password,
                             "full_name": first_name,
                             "gender": gender,
                             "institute_id": institute_id,
                             "age": age,
                             "user_type": user_type,
                             "score": 0,
                             "right_ans": 0,
                             "num_of_questions": 0}
                users.insert_one(user_data)
                print("Register success")
                return True
            except pymongo.errors.DuplicateKeyError as err:
                print("Error signing up")
                return False

    @staticmethod
    def setUserScore(score,right_ans,num_of_questions):
        if Database.is_connected:
            Database.is_logging_in = True
            db = Database.client.get_database(DATABASE)
            users = db.get_collection(USERS_COLLECTION)
            user = users.find_one({"_id": Database.user_id})
            new_score = int(user["score"]) + score
            update = {
                    "$set": {
                        "score": new_score,
                        "right_ans": right_ans,
                        "num_of_questions": num_of_questions
                    }
                    }
            users.find_one_and_update(user,update)

    @staticmethod
    def login(user_id, password):
        if Database.is_logging_in:
            return
        if Database.is_connected:
            Database.is_logging_in = True
            db = Database.client.get_database(DATABASE)
            users = db.get_collection(USERS_COLLECTION)
            data = users.find_one({"_id": user_id})
            if data is not None:
                if data["pwd"] == password:
                    Database.is_logged_in = True
                    Database.user_id = user_id
                    Database.user_type = data["user_type"]
                    print(Database.user_type)
                    print(UserType.counselor.name)
                    print("logged in as {}".format(data["user_type"]))
                    return True
            else:
                print("user not found")
                return False

    @staticmethod
    def disconnect():
        Database.is_logged_in = False
        Database.is_logging_in = False
        Database.user_type = None
        Database.user_id = None
    

    @staticmethod
    def getInstitute(institute_id):
        db = Database.client.get_database(DATABASE)
        institutes = db.get_collection(INSTITUTE_COLLECTION)
        data = institutes.find_one({"name": institute_id})
        if data is not None:
            inst = Institute(data["name"],
                        data["_id"],
                        data["num_of_students"],
                        data["counsler_id"],
                        data["rank"])
            return inst
        return None


Database.connectToServer()