from Plugins.starter import start
from Plugins.anime import Anime.py
from Plugins.manga import Manga.py
from Plugins.nhentai import Nhentai.py
from Plugins.movies import movies.py
from Plugins.tvseries import tvseries.py
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
