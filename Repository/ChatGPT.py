import openai
import os
from dotenv import load_dotenv

load_dotenv()

from Repository.Prompter import Prompter


class ChatGPT:
    def __init__(self):
        self.__openai_api_key = os.getenv('OPENAI_API_KEY')
        self.__prompter = Prompter()

    def get_post(self, theme, query):
        eng_post = self.__get_chat_gpt_answer(query)
        post = self.__prompter.generate_channel_post(theme, eng_post)
        return post

    def __get_chat_gpt_answer(self, prompt):
        openai.api_key = self.__openai_api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=600,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0)
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error generating text: {e}")
            return ""
