# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from userbot import CHANNEL, CHANNEL2
from userbot import CMD_HELP, ICON_HELP, ch2
from userbot import CMD_HANDLER as cmd
from userbot.utils import edit_delete, edit_or_reply, indomie_cmd

modules = CMD_HELP


@indomie_cmd(pattern="help(?: |$)(.*)")
async def help(indomie):
    args = indomie.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(indomie, f"{CMD_HELP[args]}\n\n© {ch2}")
        else:
            await edit_delete(indomie, f"`{args}`**NGETIK YANG BENER NGENTOT!!.**")
    else:
        memek = await indomie.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await edit_or_reply(
            indomie,
            f"**• List Help [IndomieUserbot](https://github.com/IndomieGorengSatu/IndomieUserbot):**\n\n"
            f"**• Jumlah** `{len(CMD_HELP)}` **Modules**\n"
            f"**• Bᴏᴛ Oᴡɴᴇʀ :** [{memek.first_name}](tg://user?id={memek.id})\n\n"
            "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
            f"{ICON_HELP}   {string}"
            f"\n\nSupport @{CHANNEL}"
            f"\nSupport @{CHANNEL2}",
        )
        await indomie.reply(
            f"\n**Contoh Ketik** `{cmd}help ping` **Untuk Melihat Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba yahahaha...**"
        )
