# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from indomie import CMD_HANDLER as cmd
from indomie import CMD_HELP, owner
from indomie.utils import indomie_cmd
import random
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@indomie_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@IndomieGantengV3", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya), reply_to=event.reply_to_msg_id,
            caption=f"**Asupan by** {owner}")

        await event.delete()
    except Exception:
        await event.edit("**Tidak dapat menemukan video asupan.**")


@indomie_cmd(pattern="desahcewe$")
async def _(event):
    memek = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahannya = [
            desah
            async for desah in event.client.iter_messages(
                "@IndomieGanteng", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahannya), reply_to=event.reply_to_msg_id,
            caption=f"**Desahan by** {owner}")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan vn desah.**")


@indomie_cmd(pattern="desahcowo$")
async def _(event):
    memek = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcowo = [
            desahnya
            async for desahnya in event.client.iter_messages(
                "@desahancowokkkk", filter=InputMessagesFilterVoice
            )
	]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahcowo), reply_to=event.reply_to_msg_id,
            caption=f"**Desahan cowo by** {owner}")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan desahan cowo.**")


@indomie_cmd(pattern="ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@IndomieGantengV2", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya), reply_to=event.reply_to_msg_id,
            caption=f"**Ayang by** {owner}")

        await event.delete()
    except Exception:
        await event.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}desahcewe`\
        \n  •  **Function : **Mengirim voice desah cewe secara random.\
	\n\n  •  **Syntax :** `{cmd}desahcowo`\
        \n  •  **Function :**Mengirim voice desah cowo secara random.\
        \n\n  •  **Syntax :** `{cmd}ayang`\
        \n  •  **Function : **Mencari ayang buat cowok yang jomblo.\
    "
    }
)
