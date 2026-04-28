# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base.modules import *

load_dotenv()
client = MongoClient(os.getenv("mongo_db"), server_api=ServerApi('1'))
db = client["gb"]
usr = db["user"]
net = db["network"]

#register
def ExistUser(id: int) -> bool:
    return usr.find_one({"_id": id}) is not None

def ToSAccepted(id: int) -> bool:
    user = usr.find_one({"_id": id})
    return user["tos"]

def UserRegister(id: int):
    new_user = {
        "_id": id,
        "wallet": 50,
        "tos": False,
        "study": 0,
        "healthy": 10,
        "level": 0,
        "job": None,
        "last_action": {
            "work": "",
            "study": "",
            "exam": {
                "date": "",
                "id": ""
            }
        }
    }
    usr.insert_one(new_user)

def Check(id: int, value: str):
    user = usr.find_one({"_id": id})
    return user[value]

def Pay(id: int, amount: int):
    user = {"_id": id}
    new_balance = {"$inc": {"wallet": amount}}
    usr.update_one(user, new_balance)

class LastAction:
    @staticmethod
    def Check(id: int, option: str) -> str:
        user = usr.find_one({"_id": id})
        return user.get("last_action", {}).get(option, "")

    @staticmethod
    def Update(id: int, option: str, value: str):
        usr.update_one(
            {"_id": id},
            {"$set": {f"last_action.{option}": value}}
        )

class Education:
    @staticmethod
    def Update(id: int, value: int):
        user = {"_id": id}
        new_value = {f"$inc": {"study": value}}
        usr.update_one(user, new_value)