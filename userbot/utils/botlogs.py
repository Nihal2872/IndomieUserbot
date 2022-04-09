import asyncio
import importlib
import logging
import sys
from pathlib import Path
from random import randint
import os
import random
import time
from random import randint

from telethon.errors import (
    BotMethodInvalidError,
    ChannelPrivateError,
    ChannelsTooMuchError as penuh_tolol,
    ChatAdminRequiredError,
    UserNotParticipantError,
)
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest as oh,
    InviteToChannelRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import ChatAdminRights, InputChatUploadedPhoto, InputMessagesFilterDocument
from telethon.tl.types import ChatPhotoEmpty as jembut
from telethon.utils import get_peer_id

import heroku3

from userbot import BOTLOG_CHATID, tgbot, bot, HEROKU_API_KEY, HEROKU_APP_NAME, LOGS, BOT_USERNAME

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None

# by : kenkan
async def autopilot():
    if BOTLOG_CHATID and str(BOTLOG_CHATID).startswith("-100"):
      return
    k = []  # To Refresh private ids
    async for x in bot.iter_dialogs():
        k.append(x.id)
    if BOTLOG_CHATID:
        try:
            await bot.get_entity(int("BOTLOG_CHATID"))
            return
        except BaseException:
            del heroku_var["BOTLOG_CHATID"]
    try:
        r = await bot(
            penuh_tolol(
                title ="Log UserBot",
                desc ="Group Log IndomieUserBot.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✦ Powered By ~ @IndomieProject ✦",
                megagroup=True,
            ),
        )

    except penuh_tolol:
        LOGS.info(
            "terlalu banyak channel dan grup, hapus salah satu dan restart lagi"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "terjadi kesalahan, buat sebuah grup lalu isi id nya di config var BOTLOG_CHATID."
        )
        exit(1)
    chat = r.chats[0]
    chat_id = r.chats[0].id
    if not str(chat_id).startswith("-100"):
        heroku_var["BOTLOG_CHATID"] = "-100" + str(chat_id)
    else:
        heroku_var["BOTLOG_CHATID"] = str(chat_id)

    if isinstance(chat.photo, jembut):

        memek = "userbot/resources/IndomieUserbot Botlogs.png"
        try:
            await bot(
                oh(int(chat_id), await bot.upload_file(memek)))
        except BaseException as er:
            LOGS.exception(er)
        os.remove(memek)
