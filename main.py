import time
import random
from Repository.ThemeScraper import ThemeScraper
from Repository.Prompter import Prompter
from Repository.ChatGPT import ChatGPT
from Repository.TgBot import TgBot
from Repository.Timer import Timer
from background import keep_alive


def main():
    scraper = ThemeScraper()
    prompter = Prompter()
    gpt = ChatGPT()
    bot = TgBot()
    timer = Timer()
    keep_alive()
    while True:
        if timer.should_post():
            theme = scraper.get_theme()
            bot.send_theme(theme)
            query = prompter.generate_query(theme)
            post = gpt.get_post(theme, query)
            bot.send_post(post)
        time.sleep(random.randint(1, 60) * 60)


if __name__ == '__main__':
    main()
