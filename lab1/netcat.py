import sys
from constants.config import config
from constants.tasks import tasks

from Client import Client
from Parser import Parser
from TaskExecutor import TaskExecutor
from clients.TcpClient import TcpClient

parser = Parser(sys.argv)
print(parser.get_params())
config = parser.get_params()

client = Client.factory(config['TYPE_OF_PROTOCOL'])
commands = parser.get_execution_commnads()

execution_task = commands.pop()
task_executor = TaskExecutor(client)
try:
    getattr(task_executor, tasks[execution_task])()
except Exception:
    print("Exception occured while trying to execute %s command" % execution_task)