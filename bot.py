#!/usr/local/bin/python

import os
import json

import requests
from flask import Flask, request

from chatbot.message import message
from chatbot.db import db
from chatbot.user import user
from chatbot.utils import *
from chatbot.design import design
from chatbot.notification import notification

app=Flask(__name__)

# initializing the db
botDB=db()

@app.route('/', methods=['GET'])
def verify():
    #verify facebook callback url
    if request.args.get("hub.mode") == "subscribe" and \
        request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            # TODO: we should define the error message in a separate place (file)
            return "Verification token mismatch", 403
        else:
            return request.args["hub.challenge"], 200
    else:
        return "Hello world", 200

# Facebook Webhook
@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(request.data)
    # botDB.insert(["webhook", request.query_string])
    if "object" in data and data["object"] == "page":
        # Parsing message
        botMessage=message(data)
        # Get user info
        userInfo=user(botMessage.getSenderID())
        # Response based on the defined bot flow
        botDesign=design(message=botMessage, user=userInfo, db=botDB)
    else:
        pass
    return "ok", 200

# Twiiter news updates
@app.route('/twitter', methods=['POST'])
def updateTwitter():
    log(request.data)
    data = request.get_json()
    # Notify subscribers
    botNotification=notification(botDB)
    botNotification.informSubscribers(data["text"])
    return "ok", 200

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()