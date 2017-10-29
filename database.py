from tag import Tag

class Database:
    def __init__(self):
        self.universal = dict()

        self.days   = dict()
        self.hours  = dict()

    def add(self, item, *topics):
        tag = Tag(*topics)
        self.universal[tag]      = item
        self.days[tag.datehash]  = tag
        self.hours[tag.hourhash] = tag
