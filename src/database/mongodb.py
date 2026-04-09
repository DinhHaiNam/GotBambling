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
col = db["user"]

def ExistUser(id: int) -> bool:
    return col.find_one({"_id": id}) is not None

def ToSAccepted(id: int) -> bool:
    user = col.find_one({"_id": id})
    return user["tos"]

def UserRegister(id: int):
    new_user = {
        "_id": id,
        "wallet": 500000,
        "tos": False,
        "study": 0,
        "level": 0,
        "last_action": [
            {
                "work": "",
                "study": ""
            }
        ]
    }
    col.insert_one(new_user)

def CheckWallet(id: int) -> int:
    user = col.find_one({"_id": id})
    return user["wallet"]

def Pay(id: int, amount: int):
    user = {"_id": id}
    new_balance = {"$inc": {"wallet": amount}}
    col.update_one(user, new_balance)

def Update(id: int, name: str, option: str, value): #set, inc, ...
    user = {"_id": id}
    new_value = {f"${option}": {name: value}}
    col.update_one(user, new_value)

class LastAction:
    @staticmethod
    def Check(id: int, option: str) -> str:
        user = col.find_one({"_id": id})
        return user["last_action"][0][option]
    
    @staticmethod
    def Update(id: int, option: str, value: str):
        user = {"_id": id}
        last_action = {"$set": {f"last_action.0.{option}": value}}
        col.update_one(user, last_action)