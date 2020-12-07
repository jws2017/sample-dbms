reserved = ["create","insert","update","delete","select","database","table","databases","tables","index"]

class Session(object):

    def __init__(self):
        self.databases = []
        self.current_database = None
        self.database_names = []

    def new_database(self, name):
        if name in self.database_names: raise Exception("Database %s already exists".format(name))
        self.databases.append(Database(name))
        self.database_names.append(name)

    def clear_current_database(self):
        if self.current_database is not None:
            self.current_database.active = False
            self.current_database = None

    def set_database(self, database: Database):

        if database in self.databases:
            self.clear_current_database()
            database.active = True
            self.current_database = database
        else:
            raise Exception("Database %s does not exist".format(database.name))

class Database(object):

    def __init__(self, name):
        self.name = name
        self.active = False
        self.tables = []
        self.table_id = 1
        self.table_names = []

    def create_table(self, name):
        if name in self.table_names: raise Exception("Database already contains table " + name)
        self.tables.append(Table(name, table_id, self))
        self.table_names.append(name)
        self.table_id = self.table_id + 1

class Table(object):
    def __init__(self, name, id, database):
        self.name = name
        self.id = id
        self.database = None

def parse_command(command: str) -> list:
    """
    Converts sql script to a tree form for interpretation.
    I implemented the tree as a Python list for convenience.
    expected results:
        "CREATE database;" -> ['database', 'CREATE']
        "USE database;" -> ['database', 'USE']
        "INSERT INTO dog_table VALUES ('Brent');" -> [("Brent"), 'VALUES', 'dog_table', 'INSERT']"""
    tree = [] #initialize the output tree
    tokens = command.rsplit()
    if tokens[0].casefold() == "use":
        tree.append(tokens[1])
        tree.append("USE")
    return tree

def set_database(to_use):
    pass

def interpret(tree):
    try:
        k = tree.pop()
    except IndexError:
        return 2
    else:
        if k == "use":
            to_use = tree.pop()
            set_database(to_use)
    return 1

if __name__ == "__main__":
    this = start_session()
    print("Hello, please enter an SQL command for testing.")
    print(parse_command(input()))
