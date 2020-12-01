import re
actions = ["CREATE", "CREATE TABLE", "CREATE INDEX", "USE", "INSERT", "DELETE", "UPDATE", "SELECT"]
tree = []
try:
	file = open("<insert sql script here>.sql", 'r')
	sql = file.read.split(';')
except FileNotFoundError:
	print("File not found")
finally:
	file.close()

for command in sql:
	for action in actions:
		pattern = action + "\w+"
		x = re.search(pattern, command.upper())
		if x:
			tree.append(command[len(action):])
			tree.append(action)

