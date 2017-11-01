from datetime import datetime

import uuid

class Tag:
    def __init__(self, *topics):
        self.uuid   = uuid.uuid4()
        self.topics = topics

        self.datetime   = datetime.today()
        self.datehash   = 10000 * self.datetime.year + \
                            100 * self.datetime.month + \
                                  self.datetime.day

        self.hourhash   = self.datehash * 100 + self.datetime.hour
        self.minutehash = self.hourhash * 100 + self.datetime.minute
        self.secondhash = self.minutehash * 100 + self.datetime.second

        self.microsecondhash = (self.datetime.microsecond, self.secondhash)

    def __str__(self):
        return 'Tag ({}) at {}'.format(':'.join(self.topics), str(self.datetime))

    def __repr__(self):
        return '<{}>'.format(str(self))
        
    def __hash__(self):
        return int(self.uuid) 
