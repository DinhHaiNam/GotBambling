# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import load_json
from src.database.mongodb import ExistUser, ToSAccepted
from src.base.data import command_index, embed_help

@bot.command(aliases=["h"])
async def help(ctx, option: str = None):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        if option is None:
            await ctx.send(embed=embed_help)
            return

        option = option.lower()
        cmd = command_index.get(option)

        if not cmd:
            await ctx.send("Command not found!")
            return

        aliases = cmd.get("aliases")
        aliases_msg = f"**Aliases:** {aliases}\n" if aliases else ""

        embed = discord.Embed(
            title=f"About {cmd['name']}",
            description=(
                f"**Example:** `{cmd['example']}`\n"
                f"{aliases_msg}"
                f"\n{cmd['about']}"
            )
        )

        await ctx.send(embed=embed)

    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Terms of Service")