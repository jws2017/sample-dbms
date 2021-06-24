import re


def tokenize(sql_command: str):
	"""
	Takes a single statement and parses it for SQL. The syntax of the SQL commands that will be implemented are as follows:
	create_database_statement := "CREATE DATABASE" identifier;
	identifier := [A-Za-z_][A-Za-z0-9_]*"
	select_statement := SELECT (identifier|\*) FROM identifier
	"""
	if sql_command.endswith(";"): sql_command = sql_command[:-1]
	identifier = "[A-Za-z_][A-Za-z0-9]*"
	type_ = identifier
	value_ = f"[0-9]|\".*\"|{identifier}"
	create_database_pattern = f"CREATE DATABASE {identifier}"
	create_table_pattern = f"CREATE TABLE {identifier}\W*\({identifier} {type_}(,\W*{identifier} {type_})*\)"
	create_index_pattern = f"CREATE (UNIQUE )?INDEX {identifier} ON {identifier}\W*\({identifier}(,\W*{identifier})*\)"
	where_clause = f"WHERE {identifier}={value_}"
	select_pattern = f"SELECT (({identifier}(,\W*{identifier})*)|\*) FROM {identifier}( {where_clause})?"
	update_clause = f"UPDATE {identifier}"
	set_clause = f"SET {identifier}={value_}(,\W*{identifier}={value_})*"
	update_statement = f"{update_clause}\W+{set_clause}\W+{where_clause}?"


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
	if re.match(select_pattern, sql_command, re.IGNORECASE):
		columns_end = sql_command.casefold().find("from")
		return {"action": "select", "columns": sql_command[7:columns_end], "table": sql_command[columns_end+5:]}
	if re.match(update_statement, sql_command, re.IGNORECASE):
		return {"action": "update", "table": re.match(update_clause, sql_command, re.IGNORECASE).group(0)[7:]}
