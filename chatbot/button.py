class button(object):
    def __init__(self, title, type):
        if len(title) > 20:
            raise ValueError('Button title limit is 20 characters')
        else:
            self.title = title
        self.type=type
        self.url=None
        self.payload=None

    def to_dict(self):
        data = {
            'type': self.type,
            'title': self.title
        }
        if self.type == 'web_url':
            data['url'] = self.url
        elif self.type == 'postback':
            data['payload'] = self.payload
        return data

class WebUrlButton(button):

    def __init__(self, title, url):
        button.__init__(self, title=title, type="web_url")
        self.url = url

class PostbackButton(button):

    def __init__(self, title, payload):
        button.__init__(title=title, type="postback")
        self.payload = payload