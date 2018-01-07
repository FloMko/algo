from random import randint
class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5,10)
