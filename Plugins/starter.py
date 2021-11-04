from Helper.helper import start, help , about
from pyrogram.types import InlineKeyboardButton
from config import bot
from telethon import events

class start():

    @Client.on_message(filters.command("start") & filters.private)
    async def start(bot, update): 

            buttons = [[
                         InlineKeyboardButton('😉ABOUT', callback_data='about')                    
                     ],[ 
                         Inlinekeyboardbutton("👨‍💻DEVOLOPER", url="https://t.me/N_A_V_I_P_A_V_I")
                     ]]
             
             reply_markup = InlineKeyboardMarkup(buttons)

              file='https://telegra.ph/file/de65abf86cfde85772e21.jpg'
            )
        
                                 
    @Client.on_message(filters.command(["help"]) & filters.private, group=1)
    async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    

    @Client.on_message(filters.command(["about"]) & filters.private, group=1)
    async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('HELP 🚩', callback_data='help')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
            
    
