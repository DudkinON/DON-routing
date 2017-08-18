
from urllib.parse import urlparse, parse_qs


class Router:
    def __init__(self):
        self.controller = None
        self.action = None
        self.route = None
        self.uri = None
        self.query = None

    def run(self, path):
        self.uri = urlparse(path)
        self.query = self.uri.query
        print(self.uri)
        return self.uri.path[1:]


if __name__ == '__main__':
    run = Router().run
else:
    run = Router().run


