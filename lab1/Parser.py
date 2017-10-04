from config import config
from tasks import tasks

class Parser:
    def __init__(self, args):
        self.args = args
        self.commands = []

    def get_params(self):
        if "-u" in self.args:
            config['TYPE_OF_PROTOCOL'] = '-u'
        if "-i" in self.args:
            index_of_time_interval = self.args.index("-i") + 1
            self.commands.append('PING')
            config['TIME_INTERVAL'] = int(self.args[index_of_time_interval])
        if "-max" in self.args:
            index_of_max = self.args.index("-max") + 1
            config['MAX_NR_OF_MESSAGES'] = int(self.args[index_of_max])
        if "-m" in self.args:
            index_of_message = self.args.index("-m") + 1
            config['MESSAGE'] = self.args[index_of_message]
        main_params = self.args[-2:]
        if len(main_params) == 2:
            config['HOST_NAME'] = main_params[0]
            config['PORT'] = int(main_params[1])

        return config

    def get_execution_commnads(self):
        commands = self.commands
        if len(self.commands) == 0:
            commands = tasks['SEND_MESSAGE']
        return commands