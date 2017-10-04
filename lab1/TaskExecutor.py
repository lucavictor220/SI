from time import sleep

from constants.config import config


class TaskExecutor:
    def __init__(self, client):
        self.client = client

    def send_message(self):
        self.client.send_message(config['MESSAGE'])

    def ping(self):
        print('Start ping command!\n')
        for index in range(0, config['MAX_NR_OF_MESSAGES']):
            sleep(config['TIME_INTERVAL'])
            self.client.send_message(config['MESSAGE'])
