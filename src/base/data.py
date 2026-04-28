# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import load_json, clrscr

print("Loading data...")

study_json = load_json("src/json/study.json")
work_json = load_json("src/json/work.json")
commands_json = load_json("src/commands/commands.json")



# commands - help
all_commands = commands_json["commands"]

embed_help = discord.Embed(
    title="Got Bambling's commands",
    description="Use `gb help {commands}` for more information."
)

for category_name, command_list in all_commands.items():
    commands_ = ""

    for command in command_list:
        commands_ += f"`{command['name']}` "

    embed_help.add_field(
        name=category_name,
        value=commands_,
        inline=False
    )

command_index = {
    cmd["name"]: cmd
    for cmds in commands_json["commands"].values()
    for cmd in cmds
}

print("Data completely loaded!")
time.sleep(1)
clrscr()
