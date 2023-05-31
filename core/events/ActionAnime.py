from core.base import Event, IncomingMessage
from core import Pythogram


class ActionAnime(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['список аниме']

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = 'https://v2.vost.pw/\nhttps://animego.org/\nhttps://yummyani.me/'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
