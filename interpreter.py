SQL_Integer = type("INTEGER", (int, ), {})
SQL_String = type("VARCHAR", (str, ), {})

class Session:
  
  def __init__(self):
    self.interpreter = Interpreter()
    self.id = "<placeholder>" #placeholder id for future implementation
    self.databases = []
    self.database_names = []
    self.current = None
    
  def create_database(self, name):
    if name in self.database_names:
      print("Database %s already exists".format(name))
      return 1 # database already exists
    else:
      db = Database(name)
      self.databases.append(db)
      self.database_names.append(name)
      return db
    
  def clear_current(self):
    if self.current is not None:
      self.current = None
      print("The current active database has been cleared")
    else:
      print("There is no active database")
      
  def set_current(self, db):
    if db not in self.databases:
      print("Database %s does not exist".format(db.name))
    elif db == self.current:
      print("%s is already the current database".format(db.name))
    else:
      self.current = db
      print("%s is now the current database".format(db.name))
      
    def start_session(id=None):
      if id is None:
        return Session()
      else:
        pass #to implement restarting a session by its unique id
    
    def stop(self):
      pass #to implement stopping current database session.
    
    def commit(self):
      pass #to implement saving the current session to disk
    
    def rollback(self):
      pass #to implement rollback

class Database:
  
  def __init__(self, name):
    self.name = name
    self.tables = []
    self.names = []
    
  def create_table(name, fields):
    if name in self.names:
      print("Table %s already exists".format(name))
      return 1 # Table already exists
    else:
      t = Table(name, fields)
      self.tables.append(t)
      self.names.append(t.name)
      return 0 # Table successfully created
      
  def drop_table(name):
    if name not in self.names:
      print("Table " + name + " does not exist")
      return 2 # Table does not exist
    else:
      for table in self.tables:
        if table.name == name:
          self.tables.remove(table)
          self.names.remove(name)
          return 0 # Operataion successful

class Table:
  
  def __init__(self, name, fields):
    if fields is not None:
      self.name = name
      self.fields = fields
      self.fieldnames = []
      self.records = []
      for field in fields:
        self.fieldnames.append(field.name)
    else:
      return None
    
  def new_field(name, type):
    if name in self.fieldnames:
      print("Field already exists")
      return 1 #field already exists
    else:
      pass
  
  def insert(record):
    if len(self.fields) == len(record):
      
    else:
      return 2 # cannot insert record
  
  def update(record, where):
    pass
  
  def delete(record):
    pass

class Record:
  def __init__(self):
    pass

class Field:
  def __init__(self, name, type):
    self.name = name
    self.type = type
  
class Interpreter:
  def __init__(self):
    pass
    
  def

class Token:
  def __init__(self, type, v):
    if type(v) == type:
      self.type = type
      self.v = v
    else:
      raise Exception("Type does not match value")

if __name__ == "__main__":
  print("Starting a python db session")
  session = start_session()
  print("Please enter an SQL command to execute")
  command = input()
  session.execute(command)
