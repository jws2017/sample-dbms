def tokenize(sql_command: str):
	""""""
	first_word = sql_command[:sql_command.find(" ")].casefold()
	if first_word == "create":
		return {"action": "create", "object_type": "database", "name": sql_command[len(first_word)+1:]}
