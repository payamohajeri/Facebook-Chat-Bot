import json

class message(object):
    def __init__(self, data):
        self.data = data
        self.sender_id = None
        self.recipient_id = None
        self.message_text = None
        self.message_timestamp = None
        self.parse()

    def parse(self):
        for entry in self.data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    self.parseMessage(messaging_event)

    def setSenderID(self, value):
        self.sender_id=value

    def setRecipientID(self, value):
        self.recipient_id=value

    def setMessageText(self, value):
        self.message_text=value

    def setMessageTimestamp(self, value):
        self.message_timestamp=value

    def parseMessage(self, event):    
        # the person facebook ID
        sender_id = event["sender"]["id"]
        self.setSenderID(sender_id)
        
        # the recipient's ID
        recipient_id = event["recipient"]["id"]
        self.setRecipientID(recipient_id)
        
        # the message's text
        message_text = event["message"]["text"]
        self.setMessageText(message_text)

        # the message's timestamp
        # message_timestamp = event["message"]["timestamp"]
        # self.setMessageTimestamp(message_timestamp)

    def getRecipientID(self):
        return self.recipient_id
