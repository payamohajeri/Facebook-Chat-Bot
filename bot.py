#!/usr/local/bin/python

import os
import sys
import json

import requests
from flask import Flask, request

from chatbot import message
from chatbot import db
from chatbot import response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    #verify facebook callback url
    if request.args.get("hub.mode") == "subscribe" and
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
    db.insert(["webhook", request])
    if data["object"] == "page":
        message=message(data)
        response=response(message.getRecipientID())
        response.send("Hello !")

    # {u'object': u'page', u'entry': [{u'id': u'1800484040206796', u'time': 1479555077725, u'messaging': [{u'timestamp': 1479555055370, u'message': {u'text': u'hey', u'mid': u'mid.1479555055370:87ecb93551', u'seq': 2}, u'recipient': {u'id': u'1800484040206796'}, u'sender': {u'id': u'1160095700743679'}}]}]}

def log(message):
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    db=db()
    app.run(debug=True)
