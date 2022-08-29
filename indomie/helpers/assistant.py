import functools
from telethon.events import InlineQuery
from telethon import Button
from telethon.tl.types import InputWebDocument

from indomie import *

user = bot.get_me()
OWNER_NAME = user.first_name
OWNER_ID = user.id
SANGE = INLINE_PIC

MSG = f"""
**IndomieUserBot**
━━━━━━━━━━━━━━━━━━━
✦ **Owner**: [{OWNER_NAME}](tg://user?id={OWNER_ID})
✦ **Assistant** : @{BOT_USERNAME}
━━━━━━━━━━━━━━━━━━━
Updates: @IndomieProject
━━━━━━━━━━━━━━━━━━━
"""


def in_owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in OWNER_ID:
                try:
                    await function(event)
                except BaseException:
                    pass
            else:
                try:
                    builder = event.builder
                    sur = builder.article(
                        title="IndomieUserbot",
                        url="https://t.me/IndomieProject",
                        description="© IndomieUserbot",
                        text=MSG,
                        thumb=InputWebDocument(
                            SANGE,
                            0,
                            "image/jpeg",
                            []),
                        buttons=[
                            [
                                Button.url(
                                    "Repository",
                                    url="https://github.com/IndomieGorengSatu/IndomieUserbot"),
                                Button.url(
                                    "Updates",
                                    url="https://t.me/IndomieProject"),
                            ]],
                    )
                    await event.answer(
                        [sur],
                        switch_pm=f"👥 ASISSTANT BOT OF {owner}",
                        switch_pm_param="start",
                    )
                except BaseException:
                    pass

        return wrapper

    return decorator


def inline():
    def flicks(func):
        tgbot.add_event_handler(func, InlineQuery)

    return flicks


def in_pattern(pat):
    def don(func):
        pattern = pat
        tgbot.add_event_handler(func, InlineQuery(pattern=pattern))

    return don


def owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in OWNER_ID:
                await function(event)
            else:
                try:
                    await event.answer(f"ASISSTANT BOT MILIK {owner}", alert=True)
                except BaseException:
                    pass

        return wrapper

    return decorator
