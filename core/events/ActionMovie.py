from core.base import Event, IncomingMessage
from core import Pythogram


class ActionMovie(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['список фильмов', 'список сериалов']

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = 'https://www.kinopoisk.ru/\nhttps://www.ivi.ru/\nhttps://more.tv/\n'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
