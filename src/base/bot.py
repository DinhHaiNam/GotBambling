# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base.modules import *

load_dotenv()
TOKEN = os.getenv("token")

intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix="gb ", intents=intents, help_command=None)