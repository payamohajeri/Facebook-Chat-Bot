class attachment(object):
    def __init__(self, type):
        self.type=type
        self.payload=None

    def setType(self, value):
        self.type=value

    def setPayload(self, value):
        self.payload=value

    def getType(self):
        return self.type

    def getPayload(self):
        return self.payload

    def to_dict(self):
        return {
            'type': self.type,
            'payload': self.payload
        }

class ImageAttachment(attachment):
    def __init__(self, url):
        attachment.__init__(self, type='image')
        self.url = url

    def setURL(self, value):
        self.url = url

    def getURL(self, value):
        return self.url

    def getPayload(self):
        return { 'url': self._url }

class TemplateAttachment(attachment):
    def __init__(self, template):
        attachment.__init__(self, type='template')
        self.template = template

    def setTemplate(self, value):
        self.template = value

    def getTemplate(self, value):
        return self.template

    def getPayload(self):
        return self.template.to_dict()
        
        