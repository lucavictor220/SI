from Parser import Parser
import sys


parser = Parser(sys.argv)
print(parser.get_params())
config = parser.get_params()
