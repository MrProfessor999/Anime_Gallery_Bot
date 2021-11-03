from Plugins.starter import start
from Plugins.anime import Anime
from Plugins.manga import Manga
from Plugins.nhentai import Nhentai
from Plugins.movies import Movies
from config import bot

try:
    start()
    Anime()
    Manga()
    Nhentai()
    Movies()

except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
