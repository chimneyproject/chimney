# This is an IDLE, if you want and IDE, make your own.
# by Kind2232 (@kind5545)
import sys
import re

# variables
cmds = ["help [command]: Lists all commands in this IDLE \n", "about: Gives information about this project \n", "say [text]: Writes the provided input to the console \n", "quit: Exits the IDLE. \n", "More commands coming soon!"]

print("Welcome to the Chimney IDLE!")
print("Type \"help\" for a complete list of commands.")
while True:
	input = input("> ")
	if input == "help":
		for i in range(len(cmds)):
			print(cmds[x])
	elif input == "about":
		print("Chimney is a programming language that was made by \n Kind2232 (@kind5545 on github). He made this mainly because he was bored, \n but also to show people how programming actually works.")
	elif "say" in input:
		print(string[3:len(input)])
	else:
		print("Hmm... That isn't a command that exists.")
