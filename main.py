from Plugins.starter import start
from Plugins.anime import Anime
from Plugins.manga import manga
from Plugins.nhentai import Nhentai
from Plugins.movies import movies
from config import bot


try:
    start()
    Anime()
    Manga()
    Nhentai()
    movies ()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
