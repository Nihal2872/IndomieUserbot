# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


from time import sleep
from secrets import choice

from indomie import CMD_HANDLER as cmd
from indomie import CMD_HELP
from indomie.utils.truthdare import Dare as d
from indomie.utils.truthdare import Truth as t
from indomie.utils import indomie_cmd, edit_or_reply as eor


Tod = ["Truth", "Dare"]


@memek_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    troll = choice(Tod)
    if trod == "":
        await tord.edit("    __Truth Or Dare ???__\n\n__Didapatkan Secara Acak__\n**      »» {troll} ««**")

    if trod == "truth":
        ah = await eor(tord, ("__Memproses Truth__")
        sleep(1)
        trth = choice(t)
        await ah.edit("__Mendapatkan Hasil Truth__\n\n**»** __Truth__ :\n**»** __{trth}__")
        return

    if trod == "dare":
        uh = await eor(tord, ("__Memproses Dare__")
        sleep(1)
        dr = choice(d)
        await uh.edit("__Mendapatkan Hasil Dare Tod__\n\n**»** __Dare__ :\n**»** __{dr}__")

        return


CMD_HELP.update(
    {
        "tod": f"**Plugin:** `tod`\
        \n\n  •  **Perintah :** `{cmd}tod`\
        \n  •  **Kegunaan :** __Mendapatkan Pilihan Secara Acak.__\
        \n\n  •  **Perintah :** `{cmd}tod <truth/dare>`\
        \n  •  **Kegunaan :** __Untuk Mendapatkan Truth or Dare Secara Acak.__\
    "
    }
)