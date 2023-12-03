# This is an IDLE, if you want and IDE, make your own.
# by Kind2232 (@kind5545)
import sys
import re

# variables
cmds = ["help [command]: Lists all commands in this IDLE \n", "about: Gives information about this project \n", "say [text]: Writes the provided input to the console \n", "quit: Exits the IDLE. \n", "More commands coming soon!"]

print("Welcome to the Chimney IDLE!")
print("Type \"help\" for a complete list of commands.")
while True:
	input = input("chimney> ")
	if input == "help":
		for i in range(len(cmds)):
			print(cmds[x])
