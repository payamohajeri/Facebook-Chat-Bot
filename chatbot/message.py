import json

class message(object):
    def __init__(self, data):
        self.data = data
        self.sender_id = None
        self.recipient_id = None
        self.message_text = None
        self.message_timestamp = None
        self.message_payload = None
        self.type = "unknown"
        self.parse()

    def parse(self):
        for entry in self.data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    self.parseMessage(messaging_event)
                elif messaging_event.get("postback"):
                    self.parsePostback(messaging_event)
                else:
                    pass

    def setSenderID(self, value):
        self.sender_id=value

    def setRecipientID(self, value):
        self.recipient_id=value

    def setMessageText(self, value):
        self.message_text=value

    def setMessageTimestamp(self, value):
        self.message_timestamp=value

    def setMessagePayload(self, value):
        self.message_payload=value

    def setType(self, value):
        self.type=value

    def parseMessage(self, event):        
        # the message's text
        message_text = event["message"]["text"]
        self.setMessageText(message_text)
        self.getMessageInfo(event)
        self.setType("text")

    def parsePostback(self, event):
        #get postpack
        message_payload = event["postback"]["payload"]
        self.setMessagePayload(message_payload)
        self.getMessageInfo(event)
        self.setType("postback")

    def getRecipientID(self):
        return self.recipient_id

    def getSenderID(self):
        return self.sender_id

    def getType(self):
        return self.type

    def getMessageText(self)
        return self.message_text

    def getMessagePayload(self):
        return self.message_payload

    def getMessageInfo(self, event):
        # the person facebook ID
        sender_id = event["sender"]["id"]
        self.setSenderID(sender_id)
        
        # the recipient's ID
        recipient_id = event["recipient"]["id"]
        self.setRecipientID(recipient_id)

        # the message's timestamp
        message_timestamp = event["timestamp"]
        self.setMessageTimestamp(message_timestamp)
