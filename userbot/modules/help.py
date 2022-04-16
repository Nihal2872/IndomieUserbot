# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.events import register

modules = CMD_HELP


@indomie_cmd(pattern="help(?: |$)(.*)")
async def help(indomie):
    """ For .help command,"""
    args = indomie.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await indomie.edit(str(CMD_HELP[args]))
        else:
            await indomie.edit("**`NGETIK YANG BENER NGENTOT!`**")
            await asyncio.sleep(50)
            await indomie.delete()
    else:
        memek = await event.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ✦  "
        await indomie.edit(f"**• List Help [IndomieUserbot](https://github.com/IndomieGorengSatu/IndomieUserbot):**\n\n"
                           f"**• Jumlah** `{len(CMD_HELP)}` **Modules**\n"
                           f"**• Bᴏᴛ Oᴡɴᴇʀ :** [{memek.first_name}](tg://user?id={memek.id})\n\n"
                           "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                           f"✦ {string}✦\n\n"
                           "\n\nSupport @IndomieProject",
        )
        await indomie.reply(
            f"\n✎ **ɴᴏᴛᴇꜱ :** `<{cmd}help ping>` **Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba yahahaha...**")
