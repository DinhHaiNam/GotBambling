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
        "tos": 0,
    }
    col.insert_one(new_user)
    print(f"Registered for user: {id}")

def CheckWallet(id: int) -> int:
    user = col.find_one({"_id": id})
    return user["wallet"]

def Pay(id: int, option: str, amount: int):
    user = {"_id": id}

    if option == "increase":
        new_balance = {"$inc": {"wallet": amount}}
        log = f"{id}'s wallet increased {amount}"

    elif option == "decrease":
        new_balance = {"$inc": {"wallet": -amount}}
        log = f"{id}'s wallet decreased {amount}"
        
    col.update_one(user, new_balance)
    print(log)