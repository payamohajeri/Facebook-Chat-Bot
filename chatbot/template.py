class template(object):
    def __init__(self, type):
        self.type = type

class GenericTemplate(template):
    def __init__(self, elements):
        super(GenericTemplate, self).__init__(type='generic')
        self.elements=None
        self.setElements(elements)
        
    def getElements(self):
        return self.elements

    def setElements(self, value):
        if not isinstance(value, list):
            raise ValueError(
                'elements should be a list of Element'
                )
        else:
            self.elements=value

    def to_dict(self):
        return {
            'template_type': self.type,
            'elements': [
                element.to_dict() for element in self.elements
            ]
        }

class ButtonTemplate(template):
    def __init__(self, text, buttons):
        super(ButtonTemplate, self).__init__(type='button')
        self.text = text
        self.buttons=None
        self.setButtons(buttons)

    def setButtons(self, value):
        if not isinstance(value, list):
            raise ValueError(
                'buttons should be a list of Button'
            )
        else:
            self.buttons = value

    def to_dict(self):
        return {
            'template_type': self.type,
            'text': self.text,
            'buttons': [
                button.to_dict() for button in self.buttons
            ]
        }