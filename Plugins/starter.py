from Helper.helper import START_TXT, HELP_TXT , ABOUT_TXT
from telethon import Button
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@Anime_Gallery_Robot"))
    async def event_handler_start(event):
        await bot.send_message(
    buttons=[Button.inline(
                    "HELP❗", callback_data="HELP_TXT"
            )
                
