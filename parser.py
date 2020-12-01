import re

actions = {"CREATE ": create_database, "CREATE TABLE": create_table, "CREATE INDEX": create_index, "USE": use, "SELECT": select}

try:
	file = open("<insert sql script here>.sql", 'r')
except FileNotFoundError:
	print("File not found")
else:
	for command in file.read().split(';'):
		for test in actions.keys():
			x = re.search(test, command)
finally:
	file.close()
