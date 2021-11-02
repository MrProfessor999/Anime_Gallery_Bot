from Plugins.starter import start
from Plugins.anime import anime
from Plugins.manga import manga
from Plugins.nhentai import nhentai
from Plugins.movies import movies
from Plugins.tvseries import tvseries
from config import bot


try:
    start()
    Anime()
    Manga()
    Nhentai()
    movies()
    tvseries()

except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()
