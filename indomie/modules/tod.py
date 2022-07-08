# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
# This file is a part of <https://github.com/AyiinXd/Ayiin-Userbot>
#
# Ported by IndomieGorengSatu
# From IndomieUserbot < https://github.com/IndomieGorengSatu/IndomieUserbot >
#
# Kalo mau ngecopas, jangan hapus credit ya goblok


from time import sleep
import random

from indomie import CMD_HANDLER as cmd
from indomie import CMD_HELP
from indomie.utils.tod import Dare as d
from indomie.utils.tod import Truth as t
from indomie.utils import indomie_cmd, edit_or_reply


Tod = ["Truth", "Dare"]


@indomie_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    troll = random.choice(Tod)
    if trod == "":
        await tord.edit(f"__Truth Or Dare ???__\n\n__Didapatkan Secara Acak__\n**»» {troll} ««**")

    if trod == "truth":
        ah = await edit_or_reply(tord, "__Memproses Truth__")
        sleep(1)
        trth = random.choice(t)
        await ah.edit(f"__Mendapatkan Hasil Truth__\n\n**»** __Truth__ :\n**»** __{trth}__")
        return

    if trod == "dare":
        uh = await edit_or_reply(tord, "__Memproses Dare__")
        sleep(1)
        dr = random.choice(d)
        await uh.edit(f"__Mendapatkan Hasil Dare Tod__\n\n**»** __Dare__ :\n**»** __{dr}__")

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
