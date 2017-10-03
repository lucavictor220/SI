from config import config


class Parser:
    def __init__(self, args):
        self.args = args
        self.params = []
        self.hostname = "localhost"
        self.port = 80
        self.type_of_transport_protocol = "-t"
        self.time_interval = 0
        self.max_nr_of_messages = 10

    def get_params(self):
        # posibil nici nu trebuie caci este default tcp
        if "-t" in self.args:
            print("we gonna have tcp connection")
            config['TYPE_OF_PROTOCOL'] = '-t'
        if "-u" in self.args:
            print("we gonna have udp connection")
            config['TYPE_OF_PROTOCOL'] = '-u'
        if "-i" in self.args:
            index_of_time_interval = self.args.index("-i") + 1
            print("time interval is: ", self.args[index_of_time_interval])
            config['TIME_INTERVAL'] = int(self.args[index_of_time_interval])
        if "-max" in self.args:
            index_of_max = self.args.index("-max") + 1
            print("max: ", self.args[index_of_max])
            config['MAX_NR_OF_MESSAGES'] = int(self.args[index_of_max])
        main_params = self.args[-2:]
        if len(main_params) == 2:
            print('set main params')
            config['HOST_NAME'] = main_params[0]
            config['IP'] = int(main_params[1])

        return config
