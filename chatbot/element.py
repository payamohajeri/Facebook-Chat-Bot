class element(object):
    def __init__(self, title, item_url=None,
                    image_url=None, subtitle=None, buttons=None):
        self.title = title
        self.item_url = item_url
        self.image_url = image_url
        self.subtitle = subtitle
        self.buttons = buttons

    def getTitle(self):
        return self.title

    def getSubtitle(self):
        return self._subtitle

    def to_dict(self):
        data = {
            'title': self.title,
            'item_url': self.item_url,
            'image_url': self.image_url,
            'subtitle': self.subtitle
        }
        if self.buttons:
            data['buttons'] = [
                button.to_dict() for button in self.buttons
            ]
        else:
            pass
        return data