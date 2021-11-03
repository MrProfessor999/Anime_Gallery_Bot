from Plugins import starter.py
from Plugins import Anime.py
from Plugins import Manga.py
from Plugins import Nhentai.py
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
