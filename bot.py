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
    db.insert(["webhook", json.dumps(request)])
    if data["object"] == "page":
        message=message(data)
        response=response(message.getRecipientID())
        response.send("Hello !")

def log(message):
    print str(message)
    sys.stdout.flush()

if __name__ == '__main__':
    db=db()
    app.run(debug=True)
