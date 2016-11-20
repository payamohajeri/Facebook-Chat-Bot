from chatbot.constant import _db_link
import redis

class db(object):
    def __init__(self):
        self.db=None
        self.initRedis()
        
    def initRedis(self):
        link=_db_link
        db = redis.from_url(link)
        self.setDB(db)

    def setDB(self, value):
        self.db=value

    def insert(self, value):
        self.db.set(value[0], value[1])

    def subscribe(self, value):
        self.db.sadd('subscibers', value)