from userbot import CMD_HELP, owner
from userbot import CMD_HANDLER as cmd
from userbot.events import register


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


CMD_HELP.update({
    "gabut": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}p`"
    "\n↳ : Memberi Salam"
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}l`"
    "\n↳ : Menjawab Salam."
})
