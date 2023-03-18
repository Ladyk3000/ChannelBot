from googletrans import Translator


class Prompter:
    def __init__(self):
        self.__translator = Translator()
        self.__start_query = 'write a very short under 300 symbols essay in an informal style on the topic: '
        self.__end_conv = '.'
        self.start_post = 'Сегодня я бы хотел поговорить о том, как *'

    def generate_query(self, theme: str) -> str:
        theme_q = self.__translator.translate(text=theme, src='ru', dest='en')
        query = f"{self.__start_query}{theme_q.text}".rstrip() + self.__end_conv
        return query

    def generate_channel_post(self, theme: str, english_text: str) -> str:
        post = f"{self.start_post.replace('*', theme)}{self.__translator.translate(text=english_text, src='en', dest='ru').text}".rstrip() + self.__end_conv
        return post
