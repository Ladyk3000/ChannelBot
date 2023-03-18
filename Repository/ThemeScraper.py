import requests
from bs4 import BeautifulSoup
import random
import re


class ThemeScraper:
    def __init__(self, src_url='https://www.denvistorii.ru/'):
        self.__src_url = src_url
        self.__event_class = 'masonry-item'
        self.__event_end = 'Читать полностью'
        self.__events = []
        self.theme = None

    def __get_events(self) -> None:
        try:
            html = requests.get(self.__src_url).text
            soup = BeautifulSoup(html, 'lxml')
            self.__events = soup.find_all("div", {"class": self.__event_class})
        except Exception as e:
            print(f'smth wrong {e.message, e.args}')

    def __get_themes(self) -> list:
        if not self.__events:
            self.__get_events()
        themes = []
        for event in self.__events:
            theme = re.sub(r'\s+', ' ', event.text.split(self.__event_end)[0]).strip()
            themes.append(theme)
        return themes

    def get_theme(self):
        return random.choice(self.__get_themes())
