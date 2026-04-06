from src.base.modules import *
from src.database.mongodb import *

load_dotenv()
TOKEN = os.getenv("token")

intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="gb", intents=intents, help_command=None)