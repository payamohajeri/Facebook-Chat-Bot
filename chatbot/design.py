from chatbot.response import response
from chatbot.button import WebUrlButton
from chatbot.button import PostbackButton
from chatbot.template import ButtonTemplate
from chatbot.template import GenericTemplate
from chatbot.attachment import TemplateAttachment
from chatbot.utils import *
from chatbot.element import element

class design(object):

    # in this class we define the bot flow and steps that user interact with

    def __init__(self, message, user, db):
        self.message = message
        self.user = user
        self.db = db
        self.botResponse=response(self.message.getSenderID())
        self.start()

    def start(self):
        message_type = self.message.getType()
        if message_type == "text":
            self.processText()
        elif message_type == "postback":
            self.processPostback()
        else:
            # we couldn't match the event with our handled events
            self.unknownMessage()

    def processText(self):
        # TODO: we should use AI tools / word dictionary to find out
        # more greeting statments.
        # for manual definition, we can also write them in a file and read
        # the file here to check the message text.
        if self.message.getMessageText() == "hey" or \
           self.message.getMessageText() == "hello" or \
           self.message.getMessageText() == "hi" or \
           self.message.getMessageText() == "Hi" or \
           self.message.getMessageText() == "Hello" or \
           self.message.getMessageText() == "Hey" :
           self.welcomeMsg()

        else:
            self.unknownMessage()

    def processPostback(self):
        if self.message.getMessagePayload() == "Subscribe":
            self.db.subscribe(self.message.getSenderID())
            self.botResponse.sendText("Wow "+str(self.user.getFirstname())+ \
                "! you successfully subscribed :).")
            self.exploreMsg()

        elif self.message.getMessagePayload() == "NotNow":
            self.botResponse.sendText("OK "+str(self.user.getFirstname())+\
                " you can subscribe later.")
            self.exploreMsg()

        elif self.message.getMessagePayload() == 'BestArticles':
            self.bestArticlesMsg()

        else:
            self.unknownMessage()

    def unknownMessage(self):
        self.botResponse.sendText("what ?! :| Please start with \"hey\" ")

    def welcomeMsg(self):
        # The first message that will be shown to user.
        self.botResponse.sendText("Hello "+str(self.user.getFirstname())+\
                "! hope you are doing well ;).")

        # TODO: we should not define the texts and urls in the code, =
        # it's better to have in a config file

        webButton = WebUrlButton(
           title='See website',
           url='https://news.ycombinator.com/'
        )

        postbackSubscribeButton = PostbackButton(
           title='Subscribe - TOP news',
           payload='Subscribe'
        )

        postbackNotNowButton = PostbackButton(
           title='Not now',
           payload='NotNow'
        )

        welcome_element=element(
            title='Welcome to the Chatbot Hacker News',
            item_url='https://news.ycombinator.com/',
            image_url='https://news.ycombinator.com/favicon.ico',
            subtitle='Start by subscribing to the top news',
            buttons=[
                webButton, postbackSubscribeButton, postbackNotNowButton
            ]
        )

        attachment = TemplateAttachment(template=GenericTemplate([ welcome_element ]))
        self.botResponse.sendAttachment(attachment)

    def exploreMsg(self):
        # explore menu
        webButton = WebUrlButton(
           title='See website',
           url='https://news.ycombinator.com/'
        )

        postbackFindArticlesButton = PostbackButton(
           title='Find bests',
           payload='BestArticles'
        )

        explore_template = ButtonTemplate(
            text='Do you want to explore ?',
            buttons=[
                webButton, postbackFindArticlesButton
            ]
        )

        attachment = TemplateAttachment(template=explore_template)
        self.botResponse.sendAttachment(attachment)

    def bestArticlesMsg(self):
        # The article data should be read from database, 
        # This is just for sample.
        # http://debarghyadas.com/writes/the-top-100-hacker-news-posts-of-all-time/
        articles=[
            {
                "link":"http://www.apple.com/stevejobs/",
                "title":"Steve Jobs has passed away",
                "description":"The devastating news of one of the passing of one of modern technology's biggest icons."
            },
            {
                "link":"http://news.ycombinator.com/vote?for=3742902&dir=up&whence=%6e%65%77%65%73%74",
                "title":"Show HN: This up votes itself",
                "description":"A quirky little HN hack that upvotes itself with a link to a GET request."
            },
            {
                "link":"http://www.businessweek.com/articles/2014-10-30/tim-cook-im-proud-to-be-gay",
                "title":"Tim Cook Speaks Up",
                "description":"In a first amongst elite corporate America, Apple's post-Jobs CEO openly declares his homosexuality."
            },
            {
                "link":"http://gabrielecirulli.github.io/2048/",
                "title":"2048",
                "description":"The indie-game with powers of two that addicted everybody."
            },
            {
                "link":"http://varnull.adityamukerjee.net/post/59021412512/dont-fly-during-ramadan",
                "title":"Don't Fly During Ramadan",
                "description":"The chilling tale of an American-Indian's discrimination at US airport security."
            },
        ]

        elements=[]

        for article in articles:
            webButton = WebUrlButton(
               title='View in Web',
               url=article["link"]
            )
            elements.append(element(
                    title=article["title"],
                    item_url=article["link"],
                    image_url='https://news.ycombinator.com/favicon.ico',
                    subtitle=article["description"],
                    buttons=[
                        webButton
                    ]
                )
            )
        attachment = TemplateAttachment(template=GenericTemplate(elements))
        self.botResponse.sendAttachment(attachment)










