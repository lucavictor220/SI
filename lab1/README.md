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