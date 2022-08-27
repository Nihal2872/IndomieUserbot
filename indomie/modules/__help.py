# Copyright (C) 2020 TeamDerUntergang.
#
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# @Qulec tarafından yazılmıştır.
# Thanks @Spechide.


from Indomie import BOT_USERNAME, CMD_HELP, bot, ch2
from Indomie.utils import edit_or_reply, edit_delete, indomie_cmd


@indomie_cmd(pattern="helpme ?(.*)")
async def cmd_list(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, f"**✦ Commands available in {args} ✦** \n\n" + str(CMD_HELP[args]) + "\n\n© {ch2}")
        else:
            await edit_delete(event, f"Plugins `{args}` tidak di temukan. **NGETIK YANG BENER NGENTOT!!.**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@IndomieUserbot"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await edit_delete(event,
                              f"**INLINE MODE KAMU BELUM AKTIF!!**\n** Silahkan Ikuti Tutorial dibawah ini Untuk Menyalakan Inline Mode Kamu.**\n\n**© Tutorial Untuk Menyalakan Inline Mode Kamu :**\n**❖ Silahkan pergi ke bot @BotFather ketikan** '/mybots'\n**❖ Kemudian pilih bot Assistant mu yang ada di group log**\n**❖ Lalu pilih Bot Settings > Pilih inline Mode > pilih Turn on**\n**❖ Setelah itu Pergi ke group log atau group ini lagi**\n**Ketik** `.helpme` **lagi untuk membuka menu bantuan modules nya.**"
                              )
