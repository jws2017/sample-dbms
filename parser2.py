def parse(sql:str) -> list:
    """
    Converts sql script to a tree form for interpretation by the compiler.
    I implemented the tree as a Python list for convenience.
    expected results:
        "CREATE database;" -> ['database', 'CREATE']
        "USE database;" -> ['database', 'USE']
        "INSERT INTO dog_table VALUES ('Brent');" -> [("Brent"), 'VALUES', 'dog_table', 'INSERT']"""
    tree = [] #initialize the output tree
    for command in sql.split(';'):
        tree.append(command.rsplit())
    return tree #These are Python comments Jordan
