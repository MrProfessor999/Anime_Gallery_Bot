from Helper.helper import START_TXT, HELP_TXT , ABOUT_TXT
from Telthon import button
from config import bot
from telethon import events

class start():

    @clint.on_message(filters.command('START') & filters.private)
    buttons=[Button.inline(
                    "HELP❗", callback_data="HELP_TXT"
            )
                
