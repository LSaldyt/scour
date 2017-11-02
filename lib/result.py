
class Result:
    def __init__(self, args, urls):
        self.args = args
        self.urls = urls

    def __str__(self):
        return 'Search results for: "{}" with {} results:\n    {}'.format(
                ' '.join(self.args), len(self.urls), '\n    '.join(self.urls))

    def to_link(self, url):
        return '<a href="{}">{}</a>'.format(url, url)

    def as_list(self):
        return 'Search results for "{}":\n<ol>\n{}\n</ol>'.format(
                ' '.join(self.args),
                '\n'.join('<li>{}</li>'.format(self.to_link(url)) for url in self.urls)
                )
