from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@AcuteRobot"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://telegra.ph/file/de65abf86cfde85772e21.jpg'
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@AcuteRobot"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/about"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '𝙼𝚈 𝙽𝙰𝙼𝙴: 𝙻𝚄𝙽𝙰
             𝙲𝚁𝙴𝙰𝚃𝙾𝚁: [꧁࿗༒⚔ 𝕄𝕣 ℙ𝕣𝕠𝕗𝕖𝕤𝕤𝕠𝕣⚔༒࿗꧂](https://t.meN_A_V_I_P_A_V_I/
             𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
             𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
             𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
             𝙽𝙾𝚃𝙴 
             𝚃𝙷𝙸𝚂 𝙸𝚂 𝙽𝙾𝚃 𝙰 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝚁𝙲𝙴 𝙿�𝚁𝙾𝙹𝙴𝙲𝚃'
            )
    
