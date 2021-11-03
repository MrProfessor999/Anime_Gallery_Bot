from Helper.helper import start_text, help_text , about_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@AcuteRobot"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://telegra.ph/file/de65abf86cfde85772e21.jpg')
        Start_text = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('❗HELP', callback_data='help_text'),
        InlineKeyboardButton('About me 😉', callback_data='about_text'),
    ],
    [
        InlineKeyboardButton('👨‍💻 Developer', url=f"https://t.me/N_A_V_I_P_A_V_I"),
        InlineKeyboardButton('👥 Support Group', url="https://t.me/EDIT_REPO")     
        ]]
    )

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
            
    
