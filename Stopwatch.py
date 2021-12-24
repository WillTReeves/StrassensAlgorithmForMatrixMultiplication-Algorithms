from datetime import datetime

class stopwatch:
    def __init__(self):
        self.time = None
        self.end = None

    def start(self):
        self.time = datetime.now()

    def stop(self): 
        self.end = datetime.now()
        time = self.end - self.time
        return time

    def reset(self):
        self.time = None
        self.end = None