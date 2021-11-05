from Helper.helper import START_TXT, HELP_TXT , ABOUT_TXT
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from telethon import events

class start():

    @clint.on_message(filters.command('START') & filters.private)
    async def START(client, message):
    await message.reply_text(
        text=HELPER,START_TXT
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   
                    InlineKeyboardButton("About me 😉", callback_data="ABOUT_TXT")
                    InlineKeyboardButton("HELP❗", callback_data="HELP_TXT")
                ],
                [
                    InlineKeyboardButton("DEVOLOPER", url="https://t.me/N_A_VI_P_A_V_I")
                ]
            ]
        ),
        
                                 
    @trojanz.on_message(filters.command('help') & filters.private)
    async def help(client, message):
    await message.reply_text(
        text=HELPER,HELP_TXT
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton("HOME🏘️", callback_data="START_TXT")
                ],
                [
                    InlineKeyboardButton("About me 😉", callback_data="ABOUT_TXT")
                ]
            ]
        ),

    @trojanz.on_message(filters.command('ABOUT') & filters.private)
    async def ABOUT(client, message):
    await message.reply_text(
        text=HELPER.ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   
                    InlineKeyboardButton("HOME🏘️", callback_data="START_TXT")
                ],
                [
                    InlineKeyboardButton("HELP❗", callback_data="HELP_TXT")
                ]
            ]
        ),
