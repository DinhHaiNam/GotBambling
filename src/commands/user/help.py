# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import load_json
from src.database.mongodb import ExistUser, ToSAccepted

commands_json = load_json("src/commands/commands.json")
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

@bot.command(aliases=["h"])
async def help(ctx, option: str = None):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        if option is None:
            await ctx.send(embed=embed_help)

        else:
            for category in all_commands:
                for category_name, command_list in category.items():
                    for cmd in command_list:
                        if cmd["name"] == option.lower():
                            aliases = cmd.get("aliases")
                            aliases_msg = f"**Aliases:** {aliases}\n" if aliases else ""
                            embed = discord.Embed(
                                title=f"About {option.lower()}",
                                description=(
                                    f"**Example:** `{cmd["example"]}`\n"
                                    f"{aliases_msg}"
                                    f"\n{cmd["about"]}"
                                )
                            )
                            await ctx.send(embed=embed)
                            return
                        
            await ctx.send("Command not found!")

    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")