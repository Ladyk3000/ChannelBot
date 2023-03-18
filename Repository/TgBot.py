import telebot
import os
from dotenv import load_dotenv

load_dotenv()


class TgBot:
    def __init__(self, token=os.getenv('TG_API_TOKEN'), channel=os.getenv('TG_CHANNEL'), admin=os.getenv('TG_ADMIN')):
        self.__bot = telebot.TeleBot(token)
        self.__channel = channel
        self.__admin = admin

    def send_post(self, post) -> bool:
        try:
            self.__bot.send_message(chat_id=self.__channel, text=post)
            return True
        except telebot.apihelper.ApiException:
            return False

    def send_theme(self, theme) -> bool:
        try:
            self.__bot.send_message(chat_id=self.__admin, text=f'Theme for today: {theme}')
            return True
        except telebot.apihelper.ApiException:
            return False
