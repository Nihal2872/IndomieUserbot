# Indomie Userbot
# Copyright (C) 2022-2023 @IndomieProject
#
# FROM IndomieUserbot < https://github.com/IndomieGorengSatu/IndomieUserbot >
# Kredit jangan di apus kontol
#

import time
from datetime import datetime
from secrets import choice


from indomie import CMD_HANDLER as cmd
from indomie import CMD_HELP, StartTime
from indomie import DEVS
from indomie.events import register
from .ping import get_readable_time


asben = [
    "**Eh ada Owner keren**",
    "**Hi Tuan, kemana sj?** 🤗",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Saya slalu ada buat Tuan Owner** 🥵",
    "**Hadir kak** 😉",
    "**Jangan kemana mana lagi ya bang**",
    "**Pas banget bang, aku lagi kangen**",
    "**Hadir bang** 😁",
    "**Sokap lo tai** 😡",
    "**Hadir sayang** 😚",
    "**Hadir kak maap telat** 🥺",
    "**Bang owner on juga akhirnya** 🥵",
]

rbb = [
    "**Bang owner mau off.**",
    "**Jangan off dong bang.**",
    "**Bang, mau kemana?**",
    "**Jangan lama lama bang**",
    "**Siap bang.**",
    "**Yah udah off aja bang.**",
    "**Off lagi, mau ngewe ya?**",
    "**Bang indomie, lagi ange kah?**",
    "**Jangan lupa makan bang.**",
    "**Yah pasti mao ngocok ni.**",
    "**Jangan off terus lah bang.**",
    "**Mau nonton bokep kah?**",
    "**Mau nonton lipshoe ya?**",
    "**Bang Ganteng telah off.**",
]


@register(incoming=True, from_users=DEVS, pattern=r"^cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**╼══❃ IndomieUserbot ❃══╾ **\n\n✧ **Pinger :** `{} ms`\n✧ **Uptime :** `{}`\n✧ **Owner :** `{}`\n✧ **ID :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=DEVS, pattern=r"^asben$")
async def asben(pepek):
    await pepek.reply(choice(asben))


@register(incoming=True, from_users=DEVS, pattern=r"^rbb$")
async def memek(jembut):
    await jembut.reply(choice(rbb))


CMD_HELP.update(
    {
        "asben": f"**Plugin:** `asben`\
        \n\n  •  **Perintah : **`Perintah Ini Hanya Untuk Devs Indomie Userbot.`\
        \n  •  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
