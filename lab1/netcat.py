from Parser import Parser
from TcpClient import TcpClient
from Client import Client
from TaskExecutor import TaskExecutor
from tasks import tasks
from config import config
import sys


parser = Parser(sys.argv)
print(parser.get_params())
config = parser.get_params()

client = Client.factory(config['TYPE_OF_PROTOCOL'])
commands = parser.get_execution_commnads()

execution_task = commands.pop()
print(commands)
task_executor = TaskExecutor(client)

getattr(task_executor, tasks[execution_task])()