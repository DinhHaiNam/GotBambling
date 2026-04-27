# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import load_json

study_json = load_json("src/json/study.json")
work_json = load_json("src/json/work.json")
commands_json = load_json("src/commands/commands.json")



#commands - help
all_commands = commands_json["commands"]
embed_help = discord.Embed(
        title="Got Bambling's commands",
        description="Use `gb help {commands}` for more information."
    )
for category in all_commands:
    for category_name, command_list in category.items():
        commands_ = ""     
        for command in command_list:
            commands_ += f"`{command["name"]}` "
        embed_help.add_field(
            name=category_name,
            value=commands_,
            inline=False
        )

