from .tag import Tag

from pprint import pprint

class Database:
    def __init__(self):
        self.universal = dict()
        self.days      = dict()
        self.hours     = dict()

        self.topictree = dict()

    def add(self, item, *topics):
        tag = Tag(*topics)

        self.universal[tag]      = item
        self.days[tag.datehash]  = tag
        self.hours[tag.hourhash] = tag

        level = self.add_topics(topics)
        if '__tags__' not in level:
            level['__tags__'] = []
        level['__tags__'].append(tag)

    def add_topics(self, topics):
        level = self.topictree
        for topic in topics:
            if topic not in level:
                level[topic] = dict()
            level = level[topic]
        return level

    def show_tree(self):
        pprint(self.topictree)

    def review(self, *topics):
        level = self.topictree
        for topic in topics:
            if topic not in level:
                print('Topic chain {} not found'.format(':'.join(topics)))
                return
            else:
                level = level[topic]
        self.recursive_review(level)

    def recursive_review(self, level):
        if not isinstance(level, dict):
            print('Finished')
            return
        for k, v in level.items():
            if '__tags__' in level:
                tags = level['__tags__']
                for tag in tags:
                    result = self.universal[tag]
                    print(result)
            self.recursive_review(v)

