from chatbot.constant import _access_token, _fb_url, _response_content_type
import json

class response(object):
    def __init__(self, recipient_id):
        self.access_token=_access_token
        self.content_type=_response_content_type
        self.fb_url=_fb_url
        self.recipient_id=recipient_id
        self.message_text=None

    def send(self, message_text):
        self.setMessageText(message_text)
        message=self.prepare()
        fb_response=requests.post("https://graph.facebook.com/v2.6/me/messages",
                params=message[0],
                headers=message[1],
                data=message[2]
                )
        if fb_response.status_code != 200:
            log(fb_response.status_code)
            log(fb_response.text)
        else:
            pass

    def setRecipientID(self, value):
        self.recipient_id=value

    def setMessageText(self, value):
        self.message_text=value

    def prepare(self):
        params = { "access_token": self.access_token }
        headers = { "Content-Type": self.content_type }
        data = json.dumps({
            "recipient": {
                "id": self.recipient_id
            },
            "message": {
                "text": self.message_text
            }
        })

        return [params, headers, data]