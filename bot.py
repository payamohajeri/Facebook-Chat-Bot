#!/usr/local/bin/python

import os
import json

import requests
from flask import Flask, request

from chatbot.message import message
from chatbot.db import db
from chatbot.response import response
from chatbot.user import user
from chatbot.shared import *

app=Flask(__name__)
botDB=db()

@app.route('/', methods=['GET'])
def verify():
    #verify facebook callback url
    if request.args.get("hub.mode") == "subscribe" and \
        request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        else:
            return request.args["hub.challenge"], 200
    else:
        return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    log(request.data)
    # botDB.insert(["webhook", request.query_string])
    if "object" in data and data["object"] == "page":
        botMessage=message(data)
        userInfo=user(botMessage.getSenderID())
        botResponse=response(botMessage.getSenderID())
        botResponse.send("Hello "+str(userInfo.getFirstname())+" !")
    else:
        pass
    return "ok", 200

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()