import re


def tokenize(sql_command: str):
    """
    Takes a single statement and parses it for SQL. The syntax of the SQL commands that will be implemented are as follows:
    create_database_statement := "CREATE DATABASE" identifier;
    identifier := [A-Za-z_][A-Za-z0-9_]*"
    select_statement := SELECT (identifier|*) FROM identifier
    """
    if sql_command.endswith(";"): sql_command = sql_command[:-1]
    identifier = "[A-Za-z_][A-Za-z0-9_]*"
    type_ = identifier
    value_ = f"[0-9]|\".*\"|{identifier}"

    if re.match(r"USE\W+[A-Za-z_][A-Za-z0-9_]*", sql_command, re.IGNORECASE):
        return {"action": "use", "object_type": "database", "name": (sql_command.split()[1]).strip()}
    if re.match(r"CREATE\W+DATABASE\W+[A-Za-z_][A-Za-z0-9_]*", sql_command, re.IGNORECASE):
        return {"action": "create", "object_type": "database", "name": (sql_command.split()[2]).strip()}
    if re.match(r"SHOW\W+DATABASES", sql_command, re.IGNORECASE):
        return {"action": "show", "object_type": "database"}
    if re.match(r"CREATE TABLE [A-Za-z_][A-Za-z0-9_]*\W*\([A-Za-z_][A-Za-z0-9_]* [A-Za-z_][A-Za-z0-9_]*(,\W*[A-Za-z_][A-Za-z0-9_]* [A-Za-z_][A-Za-z0-9_]*)*\)", sql_command, re.IGNORECASE):
        s = sql_command.find('(')
        if s == -1: table_name = sql_command[13:]
        else: table_name = sql_command[13:s]
        return {"action": "create", "object_type": "table", "name": table_name}
    if re.match(rf"CREATE (UNIQUE )?INDEX {identifier} ON {identifier}\W*\({identifier}(,\W*{identifier})*\)", sql_command, re.IGNORECASE):
        s = sql_command.casefold().find('on')
        name = sql_command[13:s].strip()
        table_name = sql_command[s+2:].strip()
        return {"action": "create", "object_type": "index", "name": name, "on": table_name}
    if re.match(rf"SELECT (({identifier}(,\W*{identifier})*)|\*) FROM {identifier}( {where_clause})?", sql_command, re.IGNORECASE):
        columns_end = sql_command.casefold().find("from")
        return {"action": "select", "columns": sql_command[7:columns_end], "table": sql_command[columns_end+5:]}
    if re.match(r"UPDATE\W+[A-Za-z_][A-Za-z0-9_]*\W+SET\W+[A-Za-z_][A-Za-z0-9_]*=([0-9]|\".*\"|[A-Za-z_][A-Za-z0-9_]*)(,\W*[A-Za-z_][A-Za-z0-9_]*=([0-9]|\".*\"|[A-Za-z_][A-Za-z0-9_]*))(\W+WHERE\W+[A-Za-z_][A-Za-z0-9_]*={value_})*", sql_command, re.IGNORECASE):
        return {"action": "update", "table": re.match(r"UPDATE\W+[A-Za-z_][A-Za-z0-9_]*\W+SET\W+[A-Za-z_][A-Za-z0-9_]*=([0-9]|\".*\"|[A-Za-z_][A-Za-z0-9_]*)(,\W*[A-Za-z_][A-Za-z0-9_]*=([0-9]|\".*\"|[A-Za-z_][A-Za-z0-9_]*))(\W+WHERE\W+[A-Za-z_][A-Za-z0-9_]*={value_})*", sql_command, re.IGNORECASE).group(0)[7:]}
    raise NotImplementedError

def interpret(session, tokenize_dict):
    if tokenize_dict["object_type"] == "database":
        if tokenize_dict["action"] == "create":
            return session.create_database(tokenize_dict["name"])
        if tokenize_dict["action"] == "use":
            return session.use_database(tokenize_dict["name"])
        if tokenize_dict["action"] == "show":
            return session.databases()
    raise NotImplementedError
