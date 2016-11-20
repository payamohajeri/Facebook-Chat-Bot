from chatbot.response import response
from chatbot.button import WebUrlButton
from chatbot.button import PostbackButton
from chatbot.template import ButtonTemplate
from chatbot.attachment import TemplateAttachment
from chatbot.utils import *

class design(object):
    def __init__(self, message, user, db):
        self.message = message
        self.user = user
        self.db = db
        self.botResponse=response(self.message.getSenderID())
        self.start()

    def start(self):
        message_type = message.getType()
        if message_type == "text":
            self.processText()
        elif message_type == "postback":
            self.processPostback()
        else:
            self.unknownMessage()

    def processText(self):
        if self.message.getMessageText() == "hey":
            self.welcomeMsg()
        else:
            pass

    def processPostback(self):
        if self.message.getMessagePayload() == "USER_DEFINED_PAYLOAD":
            self.botResponse.sendText("Got your postback")
        else:
            pass

    def unknownMessage(self):
        self.botResponse.sendText("what ?! :|")

    def welcomeMsg(self):
        self.botResponse.sendText("Hello "+str(self.user.getFirstname())+"! hope you are doing well ;).")

        web_button = WebUrlButton(
           title='Show website',
           url='https://petersapparel.parseapp.com'
        )

        postback_button = PostbackButton(
           title='Start chatting',
           payload='USER_DEFINED_PAYLOAD'
        )

        template = ButtonTemplate(
           text='What do you want to do next?',
           buttons=[
               web_button, postback_button
           ]
        )

        attachment = TemplateAttachment(template=template)
        self.botResponse.sendAttachment(attachment)