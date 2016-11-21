from chatbot.response import response
from chatbot.button import WebUrlButton
from chatbot.button import PostbackButton
from chatbot.template import ButtonTemplate
from chatbot.template import GenericTemplate
from chatbot.attachment import TemplateAttachment
from chatbot.utils import *
from chatbot.element import element

class notification(object):

    # This class is for notifying different subscribers with available ways

    def __init__(self, db):
        self.db = db

    def informSubscribers(self, text):
        subscribers = self.db.getSuscribers()
        for subscriber in subscribers:
            botResponse=response(subscriber)
            botResponse.sendText(str(text))