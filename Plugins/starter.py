from Helper.helper import start_text, help_text , about_text 
from pyrogram.types import InlineKeyboardButton
from config import bot
from telethon import events

class start():

    @Client.on_message(filters.command("start") & filters.private)
    async def start(bot, update): 

            buttons = [[
                         InlineKeyboardButton('My Dev 👨‍🔬', url='https://t.me/AlbertEinstein_TG'), 
                         InlineKeyboardButton('Source Code 🧾', url ='https://github.com/AlbertEinsteinTG/Adv-Auto-Filter-Bot') 
                     ],[ 
                        InlineKeyboardButton('Support 🛠', callback_data="help")
 
              reply_markup = InlineKeyboardMarkup(buttons)
              file='https://telegra.ph/file/de65abf86cfde85772e21.jpg'
            )
        await bot.send_message(
            event.chat_id,
            start_text,    
            Inlinekeyboardbutton("👨‍💻DEVOLOPER", url="https://t.me/N_A_V_I_P_A_V_I")     
                

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@AcuteRobot"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern=r"^/about$|^/about@AcuteRobot"))
    async def event_handler_about(event):
        await bot.send_message(
            event.chat_id,
            about_text
            )
            
    
