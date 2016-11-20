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
            'payload': self.getPayload
        }

class ImageAttachment(attachment):
    def __init__(self, url):
        super(ImageAttachment, self).__init__(type='image')
        self.url = url
        sefl.setPayload()

    def setURL(self, value):
        self.url = url

    def getURL(self, value):
        return self.url

    def setPayload(self):
        self.payload={ 'url': self.url }

class TemplateAttachment(attachment):
    def __init__(self, template):
        super(TemplateAttachment, self).__init__(type='template')
        self.template = template
        self.setPayload()

    def setTemplate(self, value):
        self.template = value

    def getTemplate(self, value):
        return self.template

    def setPayload(self):
        self.payload=self.template.to_dict()
        
        