# Lab 1

## General description

In this laboratory work we have to implement `netcat` command. I have chosen to implement some basic functionalities in Python.

## Usage

General form of the script usage looks as follows

`python netcat.py [flags] hostname port`

## Examples 

Send message "Ceva cu tolk" over the network to the localhost 8080

`python netcat.py -m "Ceva cu tolk" localhost 8080`

Send 10 messages with a specified frequency of 1 sec 

`python netcat.py -m "Ceva cu tolk" -i 1 -max 10 localhost 8080`

Create a tcp server which is listening to the incoming connections

`python netcat.py -l localhost 8080`

Scan ports for the specified ip address or hostname

`python netcat.py -s 1-200 37.187.181.164 80`

Get a page and save it to a file

`python netcat.py -get patria.md 80`

Create a simple proxy for message redirection. 

`python netcat.py -rt localhost 8081 localhost 8080`


## Flags

`-t | -u` - send tcp or udp packages

`-max` - number of messages to be send 

`-i` - time interval in seconds between 2 successive messages

`-s` - specify port scanning command. Next argument is of the form `1-300` with the ports to scan.

`-get` - specify the get-webpage command


## Remarks

The script should have at least 2 params: hostname and port. During parsing process script assumes you provide value if you specify parameter. (Ex: -i 1, -m "Message to send") There are still a lot of ways to have unexpected behavior of script. Generally, it should execute the first command it receives.

## Architecture

Parser class - is used in order to parse given arguments and to set global config and command to be executed.

Client class - returns a client instance for tcp or udp server. Factory pattern have been used to implement this functionality

TaskExecutor class - is responsible for executing any given command using tasks in the constants folder.

servers folder - have test servers which can be used to execute commands in the test environment.

webpages folder - is automatically created one you run script with `-get` flag in order to store webpages.

#### netcat.py

In the main script there is Parser class called to get all the configurations and commands to be executed and then we call TaskExecutor passing to it TCP/UDP client. TaskExecutor class calls internally method from the commands configuration.

```python
parser = Parser(sys.argv)
config = parser.get_params()

client = Client.factory(config['TYPE_OF_PROTOCOL'])
commands = parser.get_execution_commnads()

execution_task = commands.pop()
task_executor = TaskExecutor(client)
try:
    getattr(task_executor, tasks[execution_task])()
except error, exc:
    print("Exception occurred while trying to execute %s command" % execution_task)
    print(exc)

```


#### config.py

This configuration is responsible for all the flags send to script and which are used to describe configurations used to execute tasks.

```python
config = {
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


```


#### tasks.py

Tasks configuration describes all possible actions performed by netcat.py script.

```python
tasks = {
    'SEND_MESSAGE': 'send_message',
    'PING': 'ping',
    'CREATE_SERVER': 'server',
    'SCAN': 'scan',
    'GET_PAGE': 'get_page',
    'PROXY': 'proxy',
    'SEND_FILE': 'send_file',
    'SERVER': 'server'
}
```

#### Client class

Creates client by returning the instance of the class set by TYPE_OF_PROTOCOL configuration

```python

class Client:
    @classmethod
    def factory(cls, protocol):
        client = None
        if protocol == '-t':
            client = TcpClient(config['HOST_NAME'], config['PORT'])
        if protocol == '-u':
            client = UdpClient(config['HOST_NAME'], config['PORT'])

        return client

```