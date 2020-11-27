filename = "<insert random filename here>"
"""Opening the file to be parsed"""
try:
	file = open(filename, 'r')
	 
except FileNotFoundError:
	print("File not found)
else:
	script = file.read()
	commands = script.split(';')
finally:
	file.close()

for command in commands:
		tokens = command.split(" ")
		for token in tokens:
			parse(token)

def parse(token: str) {
	if token in keywords:
}