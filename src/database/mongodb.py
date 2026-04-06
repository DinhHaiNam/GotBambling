from src.base.modules import *

load_dotenv()
client = MongoClient(os.getenv("mongo_db"), server_api=ServerApi('1'))
db = client["nem"]
col = db["user"]

def FirstCommand(id: int) -> bool:
    return col.find_one({"_id": id}) is not None

def UserRegister(id: int):
    new_user = {
        "_id": id,
        "wallet": 500000
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