from random import randint
import time
from queue import Node, NodeQueue


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5,10)

class MediaPlayerQueue(NodeQueue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()
    def add_track(self, track):
        self.enqueue(track)
    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)
