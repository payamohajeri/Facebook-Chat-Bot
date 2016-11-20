from chatbot.constant import _fb_userinfo_url, _access_token
from chatbot.utils import *
import json
import requests

class user(object):
    def __init__(self, userID):
        self.userID=userID
        self.fb_url=_fb_userinfo_url
        self.access_token=_access_token
        self.profilePic=None
        self.firstname=None
        self.lastname=None
        self.gender=None
        self.getUserInfo()

    def getUserInfo(self):
        fb_response=requests.get(str(self.fb_url) + str(self.userID) + \
            "?fields=first_name,last_name,profile_pic,locale,timezone,gender&" + \
            "access_token=" + \
            str(self.access_token)
        )
        if fb_response.status_code != 200:
            log(fb_response.status_code)
            log(fb_response.text)
        else:
            data=fb_response.json()
            self.setProfilePic(data['profile_pic'])
            self.setFirstname(data['first_name'])
            self.setLastname(data['last_name'])
            self.setGender(data['gender'])

    def setProfilePic(self, value):
        self.profilePic=value

    def setFirstname(self, value):
        self.firstname=value

    def setLastname(self, value):
        self.lastname=value

    def setGender(self, value):
        self.gender=value

    def getProfilePic(self):
        return self.profilePic

    def getFirstname(self):
        return self.firstname

    def getLastname(self):
        return self.lastname

    def getGender(self):
        return self.gender