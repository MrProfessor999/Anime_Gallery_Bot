from Helper.helper import START_TXT, HELP_TXT , ABOUT_TXT
from telethon import Button
from config import bot
from telethon import events

class start():

    @clint.on_message(filters.command('START') & filters.private)
    await bot.send_message(
    buttons=[Button.inline(
                    "HELP❗", callback_data="HELP_TXT"
            )
                
