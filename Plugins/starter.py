from Helper.helper import START_TXT, HELP_TXT , ABOUT_TXT
from config import bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@Anime_Gallery_Robot"))
    async def event_handler_START(event):
        await bot.send_message(
            event.chat_id,
            START_TXT,                            
            file='https://telegra.ph/file/de65abf86cfde85772e21.jpg'
            )
buttons=[[InlineKeyboardButton('DEVOLOPER', url=f"https://t.me/N_A_V_I_P_A_V_I")]] 
                                                     
  

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@Anime_Gallery_Robot"))
    async def event_handler_HELP(event):
        await bot.send_message(
            event.chat_id,
            HELP_TXT
            )

    @bot.on(events.NewMessage(pattern="/about"))
    async def event_handler_ABOUT(event):
        await bot.send_message(
            event.chat_id,
            ABOUT_TXT
        )
    
