from chatbot.constant import *
import redis

class db(object):
    def __init__(self):
        self.initRedis()
        self.db=None
        
    def initRedis(self):
        link=None
        if _my_env == "production":
            link=os.environ.get("REDIS_URL")
        else:
            link="localhost:6379"
        db = redis.from_url(link)
        self.setDB(db)

    def setDB(self, value):
        self.db=value

    def insert(self, value):
        self.db.set(value[0], value[1])