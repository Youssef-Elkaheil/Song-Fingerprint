import logging

class Logger():
    def __init__(self):
        self.logger = logging.getLogger()   # Logger maintainer
        self.logger.setLevel(logging.DEBUG)
