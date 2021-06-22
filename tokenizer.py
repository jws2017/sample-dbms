import re


def tokenize(sql_command: str):
	"""
	Takes a single statement and parses it for SQL. The syntax of the SQL commands that will be implemented are as follows:
	statement := "CREATE DATABASE" identifier;
	identifier := [A-Za-z_][A-Za-z0-9_]*"
	"""
	if sql_command.endswith(";"): sql_command = sql_command[:-1]
	identifier = "[A-Za-z_][A-Za-z0-9]*"
	type_ = identifier
	create_database_pattern = f"CREATE DATABASE {identifier}"
	create_table_pattern = f"CREATE TABLE {identifier}\W*\({identifier} {type_}(,\W*{identifier} {type_})*\)"
	create_index_pattern = f"CREATE (UNIQUE )?INDEX {identifier} ON {identifier}\W*\({identifier}(,\W*{identifier})*\)"

	if re.match(create_database_pattern, sql_command, re.IGNORECASE):
		return {"action": "create", "object_type": "database", "name": sql_command[16:]}
	if re.match(create_table_pattern, sql_command, re.IGNORECASE):
		s = sql_command.find('(')
		if s == -1: table_name = sql_command[13:]
		else: table_name = sql_command[13:s]
		return {"action": "create", "object_type": "table", "name": table_name}
	if re.match(create_index_pattern, sql_command, re.IGNORECASE):
		s = sql_command.casefold().find('on')
		name = sql_command[13:s].strip()
		table_name = sql_command[s+2:].strip()
		return {"action": "create", "object_type": "index", "name": name, "on": table_name}
