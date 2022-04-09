from importlib import import_module
from sys import argv
from platform import python_version
from pytgcalls import __version__ as pytgcalls

from telethon import version
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import ALIVE_LOGO, BOT_VER as ubotversion, LOGS, BOT_TOKEN, BOT_USERNAME, BOTLOG_CHATID, bot
from userbot.modules import ALL_MODULES
from userbot.modules.asisstant import ASST_MODULES
from userbot.utils import autobot, autopilot
from userbot import call_py


INVALID_PH = '\nERROR: Nomor Telepon yang dimasukkan TIDAK VALID' \
             '\n Tips: Gunakan Kode Negara beserta nomornya.' \
             '\n atau periksa nomor telepon Anda dan coba lagi !'


try:
    bot.start()
    call_py.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

for module_name in ASST_MODULES:
    imported_module = import_module("userbot.modules.asisstant." + module_name)

if not BOTLOG_CHATID:
    LOGS.info(
        "Vars BOTLOG_CHATID laga di isi, otewe bikin grup ngeeeng..."
    )
    bot.loop.run_until_complete(autopilot())

if not BOT_TOKEN:
    LOGS.info(
        "Vars BOT_TOKEN kaga di isi, otw bikin bot di @Botfather ngeeengg..."
    )
    bot.loop.run_until_complete(autobot())


LOGS.info(
    f"Python Version - {python_version()} \
      \nTelethon Version - {version.__version__} \
      \nPyTgCalls Version - {pytgcalls.__version__} \
      \nIndomieUserbot Version - ⚙️ V{ubotversion} [ BERHASIL DIAKTIFKAN! ]")


async def sokasik():
    user = await bot.get_me()
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_file(BOTLOG_CHATID, ALIVE_LOGO, caption=f"**IndomieUserbot Berhasil Diaktifkan**\n\n✦ **Oᴡɴᴇʀ Bᴏᴛ :** [{user.first_name}](tg://user?id={user.id})\n✦ **Bᴏᴛ Vᴇʀ :** {BOT_VER}\n✦ **Sᴜᴘᴘᴏʀᴛ​ :** @IndomieProject\n✦ **Sᴛᴏʀᴇ​ :** @IndomieStore")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@IndomieProject"))
    except BaseException:
        pass
    try:
        await bot(JoinChannelRequest("@IndomieStore"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


bot.loop.run_until_complete(sokasik())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
