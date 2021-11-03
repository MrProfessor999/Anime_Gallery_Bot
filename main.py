from Plugins import starter
from Plugins import Anime
from Plugins import Manga
from Plugins import Nhentai
from config import bot

try:
    start()
    Anime()
    Manga()
    Nhentai()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
