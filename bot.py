#!/usr/local/bin/python

import os
import sys
import json

import requests
from flask import Flask, request

from chatbot.message import message
from chatbot.db import db
from chatbot.response import response

app=Flask(__name__)
botdb=db()

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
    # botdb.insert(["webhook", request.query_string])
    if data["object"] == "page":
        botmessage=message(data)
        botresponse=response(botmessage.getRecipientID())
        botresponse.send("Hello !")
    return "ok", 200

def log(message):
    print str(message)
    sys.stdout.flush()

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()