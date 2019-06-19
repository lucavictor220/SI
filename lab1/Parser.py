from constants.Config import Config
from constants.tasks import tasks


class Parser:
    def __init__(self, args):
        self.args = args
        self.commands = []

    def parse_params(self):
        config = Config()
        if "-u" in self.args:
            config.set_type_of_protocol('-u')
        if "-i" in self.args:
            index_of_time_interval = self.args.index("-i") + 1
            config.set_time_interval(self.args[index_of_time_interval])
            self.commands.append('PING')
        if "-max" in self.args:
            index_of_max = self.args.index("-max") + 1
            config.set_max_nr_of_messages(self.args[index_of_max])
        if "-m" in self.args:
            index_of_message = self.args.index("-m") + 1
            config.set_message(self.args[index_of_message])
        if "-s" in self.args:
            index_of_scan_ports = self.args.index("-s") + 1
            config.set_ports_to_scan(self.args[index_of_scan_ports])
            self.commands.append('SCAN')
        if "-l" in self.args:
            self.commands.append('SERVER')
        if "-get" in self.args:
            self.commands.append('GET_PAGE')
        if "-rt" in self.args:
            index_of_target_host_name = self.args.index("-rt") + 1
            config.set_target_host_name(self.args[index_of_target_host_name])
            config.set_target_port(self.args[index_of_target_host_name + 1])
            self.commands.append('PROXY')

        main_params = self.args[-2:]
        if len(main_params) == 2:
            config.set_host_name(main_params[0])
            config.set_port(main_params[1])

    def get_execution_commnads(self):
        commands = self.commands
        if len(self.commands) == 0:
            commands = ['SEND_MESSAGE']
        return commands
