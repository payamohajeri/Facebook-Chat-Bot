#!/usr/local/bin/python

import os
import sys
import json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    return "Hello world", 200

def log(message):
    print str(message)
    sys.stdout.flush()

def main():
    print("Bot")

if __name__ == '__main__':
    # main()
    app.run(debug=True)
