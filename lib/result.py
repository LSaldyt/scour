
class Result:
    def __init__(self, args, urls):
        self.args = args
        self.urls = urls

    def __str__(self):
        return 'Search results for: "{}" with {} results'.format(' '.join(self.args), len(self.urls))
