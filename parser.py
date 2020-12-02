import re
action = ["CREATE", "CREATE TABLE", "CREATE INDEX", "USE", "INSERT", "DELETE", "UPDATE", "SELECT"]
try:
	file = open("<insert sql script here>.sql", 'r')
	script = file.read()
	parse(script)
except FileNotFoundError:
	print("File not found")
finally:
	file.close()

"""Syntax parsing"""
def parse(sql: str):
	tree = []
	
	identifier = "[A-Za-z][A-Za-z0-9]*"
	typ = "int | String"
	coldecl = identifier + " " + typ
	
	for command in sql.split(';'):
		match_string = command.upper()
		create_table_pattern = "CREATE TABLE " + identifier + " (" + coldecl + ")"
		create_database_pattern = "CREATE " + identifier
		use_database_pattern = "USE " + identifier
		create_table = re.search(create_table_pattern, match_string)
		create_database = re.search(create_database_pattern, match_string)
		use_database = re.search(use_database_pattern, match_string)
		if create_database:
			name = create_database.string[7:]
			tree.append(name)
			tree.append("CREATE")
		if create_table:
			token = create_table.string.split(" ")
			name = token[1]
			column_name = token[2][1:]
			column_type = token[3]
			tree.append(column_name)
			tree.append(column_type)
			tree.append("COLUMN")
			tree.append(name)
			tree.append("CREATE TABLE")
		if use_database:
			name = use_database.string[4:]
			tree.append(name)
			tree.append("USE")
	return tree

""" """
def my_eval(atree):
	while len(atree) > 0:
		token = atree.pop()
		if token == "CREATE":
			name=atree.pop()
			create_database(name)
		else if token == "CREATE TABLE":
			name = atree.pop()
			coldecl = atree.pop()
