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
	typ = "int|String"
	coldecl = identifier + " " + typ
	op = "<|>|=|!="
	
	for command in sql.split(';'):
		match_string = command.upper()
		create_table_pattern = "CREATE TABLE " + identifier + " (" + coldecl + ")"
		create_database_pattern = "CREATE " + identifier
		use_database_pattern = "USE " + identifier
		insert_record_pattern = "INSERT INTO " + identifier + " VALUES (" + identifier + ")"
		select_record_pattern = "SELECT " + identifier + " FROM " + identifier
		select_where_record_pattern = "SELECT " + identifier + " FROM " + identifier + " WHERE " + identifier + " " + op + " " + identifier
		delete_record_pattern = "DELETE FROM " + identifier
		delete_where_record_pattern = "DELETE FROM " + identifier + " WHERE " + identifier + " " + op + " " + identifier
		update_record_pattern = "UPDATE " + identifier + " SET " + identifier + " = " + identifier + " WHERE " + identifier + " " + op + " " + identifier
		
		create_table = re.search(create_table_pattern, match_string)
		create_database = re.search(create_database_pattern, match_string)
		use_database = re.search(use_database_pattern, match_string)
		insert_record = re.search(insert_record_pattern, match_string)
		select_record = re.search(select_record_pattern, match_string)
		select_where_record = re.search(select_where_record_pattern, match_string)
		delete_record = re.search(delete_record_pattern, match_string)
		delete_where_record = re.search(delete_where_record_pattern, match_string)
		update_record = re.search(update_record_pattern, match_string)
		
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
		if insert_record:
			token = insert_record.string.split(" ")
			name = token[2]
			value = token[4]
			tree.append(value)
			tree.append("VALUE")
			tree.append(name)
			tree.append("INSERT INTO")
		if select_record:
			token = select_record.string.split(" ")
			name = token[3]
			col_name = token[1]
			tree.append(col_name)
			tree.append("COLUMN")
			tree.append(name)
			tree.append("SELECT FROM")
		if select_where_record:
			token = select_where_record.string.split(" ")
			name = token[3]
			col_name = token[1]
			comp = token[5]
			op = token[6]
			val = token[7]
			tree.append(val)
			tree.append(comp)
			tree.append(op)
			tree.append(col_name)
			tree.append("COLUMN")
			tree.append(name)
			tree.append("SELECT FROM")
		if delete_record:
			name = delete_record.string[12:]
			tree.append(name)
			tree.append("DELETE FROM")
		if delete_where_record:
			token = delete_where_record.string.split(" ")
			name = token[2]
			comp = token[4]
			op = token[5]
			val = token[6]
			tree.append(val)
			tree.append(comp)
			tree.append(op)
			tree.append(name)
			tree.append("DELETE FROM")
		if update_record:
			token = update_record.string.split(" ")
			name = token[1]
			attr = token[3]
			val = token[5]
			colname = token[7]
			op = token[8]
			someval = token[9]
			tree.append(someval)
			tree.append(colname)
			tree.append(op)
			tree.append(val)
			tree.append(attr)
			tree.append(name)
			tree.append("UPDATE")
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
