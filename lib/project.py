from .collect  import collect
from .database import Database

import pickle

class Project:
    def __init__(self):
        self.database   = Database()
        self.topicChain = []

    def __get_topic_str__(self):
        return ':'.join(self.topicChain)

    def switch(self, *chain):
        '''
        Change to topic to [*chain]
        Arguments: [*chain (str(s))]
        '''
        self.topicChain = chain
        print('Changed topic to :{}'.format(self.__get_topic_str__()))

    def begin(self, topic):
        '''
        Begin a new topic or sub topic, called [topic]
        If already in a topic, begins a new topic
        Arguments: [topic (str)]
        '''
        self.topicChain.append(topic)
        self.database.add_topics(self.topicChain)
        print('Beginning the topic {}'.format(topic))

    def end(self):
        '''
        End the current topic or subtopic
        Arguments: None
        '''
        if len(self.topicChain) > 0:
            topic = self.topicChain.pop()
            print('Exiting the topic {}'.format(topic))
        else:
            print('No topic to exit')

    def collect(self, *args, stop=10):
        '''
        Collect urls based on a google search with [args]
        Arguments: [*args] # A traditional google search
        '''
        print('Collecting sources for the topic: {}'.format(self.__get_topic_str__()))
        result = collect(*args, stop=stop)
        self.database.add(result, *self.topicChain)

    def show(self):
        '''
        Show the current database topic tree
        Arguments: None
        '''
        self.database.show_tree()

    def review(self, *topics):
        '''
        Review a particular topic in the project database
        Arguments: [*chain (str(s))]
        '''
        self.database.review(*topics)

    def save(self, filename):
        '''
        Create a backup of the project in the specified file
        Arguments: [filename (str)]
        '''
        print('Saving project to file: {}'.format(filename))
        with open(filename, 'wb') as outfile:
            pickle.dump(self, outfile)

    def load(self, filename):
        '''
        Load from a saved project file
        Overwrites current database
        Arguments: [filename (str)]
        '''
        print('Loading database from file: {}'.format(filename))
        with open(filename, 'rb') as infile:
            project = pickle.load(infile)
            self.database = project.database # TODO: Merge databases

    def purge(self):
        '''
        DANGEROUS:
        Purge all collected data!!!!!!
        Arguments: None
        '''
        print('Purging all collected data')
        self.database = Database()
        del self.topicChain[:]
