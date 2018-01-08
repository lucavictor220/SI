from socket import error
import sys
from constants.Config import Config
from constants.tasks import tasks

from Client import Client
from Parser import Parser
from TaskExecutor import TaskExecutor
from clients.TcpClient import TcpClient

configurationClass = Config()
parser = Parser(sys.argv)
parser.parse_params()

client = Client.factory(configurationClass.config['TYPE_OF_PROTOCOL'])
commands = parser.get_execution_commnads()

execution_task = commands.pop()
task_executor = TaskExecutor(client)
try:
    getattr(task_executor, tasks[execution_task])()
except error, exc:
    print("Exception occurred while trying to execute %s command" % execution_task)
    print(exc)