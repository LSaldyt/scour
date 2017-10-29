from search import search
from database import Database

class Project:
    def __init__(self):
        self.topics   = dict()
        self.database = Database()

        self.topicChain = []

    def switch(self, topic):
        self.topicChain = [topic]

    def push(self, topic):
        self.topicChain.append(topic)

    def pop(self):
        self.topicChain.pop()

    def collect(self, *args, stop=10):
        urls = search(*args, stop=stop)
        for url in urls:
            print(url)
        self.database.add(urls, *self.topicChain)
