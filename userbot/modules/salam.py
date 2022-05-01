from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.events import register


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇....SAYANG!!!!")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......")


CMD_HELP.update({
    "salam": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}P`"
    "\n↳ : Memberi Salam."
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}L`"
    "\n↳ : Menjawab Salam."
})


CMD_HELP.update({
    "salam2": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}atg`"
    "\n↳ : Istigfar 1."
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ast`"
    "\n↳ : Istigfar 2."
})
