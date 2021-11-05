from Helper.helper import start, help , about
from pyrogram.types import InlineKeyboardButton
from config import bot
from telethon import events

class start():

    @clint.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   
                    InlineKeyboardButton("About Me", callback_data="about_data")
                ],
                [
                    InlineKeyboardButton("BOT Channel", url="https://t.me/BOTS_GARAGE"),
                    InlineKeyboardButton("Support Group", url="https://t.me/BOTS_ASK")
                ]
            ]
        ),
        
                                 
    @trojanz.on_message(filters.command('help') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   
                    InlineKeyboardButton("About Me", callback_data="about_data")
                ],
                [
                    InlineKeyboardButton("BOT Channel", url="https://t.me/BOTS_GARAGE"),
                    InlineKeyboardButton("Support Group", url="https://t.me/BOTS_ASK")
                ]
            ]
        ),

    @trojanz.on_message(filters.command('ABOUT') & filters.private)
async def help(client, message):
    await message.reply_text(
        text=Script.About_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   
                    InlineKeyboardButton("HELP❗", callback_data="HELP")
                ],
                [
                    InlineKeyboardButton("BOT Channel", url="https://t.me/BOTS_GARAGE"),
                    InlineKeyboardButton("Support Group", url="https://t.me/BOTS_ASK")
                ]
            ]
        ),
