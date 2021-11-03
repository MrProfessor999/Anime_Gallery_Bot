from Plugins.starter import start
from Plugins.Anime import Anime
from Plugins.Manga import Manga
from Plugins.Nhentai import Nhentai
from Plugins.Movies import Movies
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
