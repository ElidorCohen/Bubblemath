import pymongo
from pymongo import MongoClient
from User import User


DATABASE = "BubbleMath"
ADMIN = "admin"
ADMIN_PASS = "GF7JmQYsRagdDIeu"
USERS_COLLECTION = "Users"

# Commands
CREATE_USER = "createUser"


class Database:
    host = "mongodb+srv://{}:{}@cluster0.r0eft.mongodb.net/{}?retryWrites=true&w=majority".format(ADMIN, ADMIN_PASS, DATABASE)
    client = MongoClient()
    is_connected = False

    @staticmethod
    def connectToServer():
        try:
            Database.client = pymongo.MongoClient(Database.host)
            Database.is_connected = True
            print("Connected")
        except pymongo.errors.ServerSelectionTimeoutError as err:
            # do whatever you need
            print(err)

    @staticmethod
    def getUser(user_id):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            users = db.get_collection(USERS_COLLECTION)
            data = users.find_one({"_id": user_id})
            if data is not None:
                user = User(data["_id"],
                            data["first_name"],
                            data["last_name"],
                            data["age"],
                            data["user_type"],
                            data["gender"])
                return user
            return None

    @staticmethod
    def register(user_id, first_name,last_name, password, gender, institute_id, age, user_type):
        if Database.is_connected:
            try:
                db = Database.client.get_database(DATABASE)
                users = db.get_collection(USERS_COLLECTION)
                user_data = {"_id": user_id,
                             "pwd": password,
                             "first_name": first_name,
                             "last_name": last_name,
                             "gender": gender,
                             "institute_id": institute_id,
                             "age": age,
                             "user_type": user_type}
                users.insert_one(user_data)
                print("registered")
            except pymongo.errors.DuplicateKeyError as err:
                print("Already Registered")

    @staticmethod
    def login(user_id, password):
        if Database.is_connected:
            db = Database.client.get_database(DATABASE)
            users = db.get_collection(USERS_COLLECTION)
            data = users.find_one({"_id": user_id})
            if data is not None:
                if data["pwd"] == password:
                    return True
            else:
                return False


Database.connectToServer()
print(Database.getUser("123").last_name)
