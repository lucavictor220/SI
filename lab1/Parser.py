from constants.config import config
from constants.tasks import tasks


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
        if "-s" in self.args:
            self.commands.append('SCAN')
            index_of_scan_ports = self.args.index("-s") + 1
            ports_array = self.args[index_of_scan_ports].split('-')
            config['PORTS_TO_SCAN'] = int(ports_array[0]), int(ports_array[1])
        main_params = self.args[-2:]
        if len(main_params) == 2:
            config['HOST_NAME'] = main_params[0]
            config['PORT'] = int(main_params[1])

        return config

    def get_execution_commnads(self):
        commands = self.commands
        if len(self.commands) == 0:
            commands = ['SEND_MESSAGE']
        return commands
