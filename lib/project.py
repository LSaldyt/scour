from .search import search
from .database import Database

class Project:
    def __init__(self):
        self.topics   = dict()
        self.database = Database()

        self.topicChain = []

    def switch(self, topic):
        '''
        Change to topic to [topic]
        Arguments: [topic (str)]
        '''
        self.topicChain = [topic]

    def begin(self, topic):
        '''
        Begin a new topic or sub topic, called [topic]
        If already in a topic, begins a new topic
        Arguments: [topic (str)]
        '''
        self.topicChain.append(topic)

    def end(self):
        '''
        End the current topic or subtopic
        Arguments: None
        '''
        self.topicChain.pop()

    def collect(self, *args, stop=10):
        '''
        Collect urls based on a google search with [args]
        Arguments: [*args] # A traditional google search
        '''
        urls = search(*args, stop=stop)
        for url in urls:
            print(url)
        self.database.add(urls, *self.topicChain)

    def purge(self):
        '''
        DANGEROUS:
        Purge all collected data!!!!!!
        Arguments: None
        '''
        self.database = Database()
