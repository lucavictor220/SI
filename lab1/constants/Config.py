class Config:
    def __init__(self):
        self.config = {
            'HOST_NAME': 'localhost',
            'PORT': 80,
            'TYPE_OF_PROTOCOL': '-t',
            'TIME_INTERVAL': 1,
            'MAX_NR_OF_MESSAGES': 5,
            'MESSAGE': 'default',
            'PORTS_TO_SCAN': (1, 100),
            'TARGET_HOST_NAME': 'localhost',
            'TARGET_PORT': 8000
        }

    def set_host_name(self, host_name):
        self.config['HOST_NAME'] = host_name

    def set_port(self, port):
        self.config['PORT'] = int(port)

    def set_type_of_protocol(self, type_of_protocol):
        self.config['TYPE_OF_PROTOCOL'] = type_of_protocol

    def set_time_interval(self, time_interval):
        self.config['TIME_INTERVAL'] = time_interval

    def set_max_nr_of_messages(self, max_nr_of_messages):
        self.config['MAX_NR_OF_MESSAGES'] = int(max_nr_of_messages)

    def set_message(self, message):
        self.config['MESSAGE'] = message

    def set_ports_to_scan(self, ports_to_scan):
        ports_array = ports_to_scan.split('-')
        self.config['PORTS_TO_SCAN'] = int(ports_array[0]), int(ports_array[1])

    def set_target_host_name(self, target_host_name):
        self.config['TARGET_HOST_NAME'] = target_host_name

    def set_target_port(self, target_port):
        self.config['TARGET_PORT'] = target_port