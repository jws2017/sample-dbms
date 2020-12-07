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
    
  def create_table(name, column_dict):
    if name in self.names:
      print("Table %s already exists".format(name))
    else:
      pass #to implement create_table
      
  def drop_table(name):
    if name not in self.names:
      print("Table " + name + " does not exist")
    else:
      pass #to implement drop_table

class Table:
  
  def __init__(self, name, columns):
    self.name = name
    self.columns = columns

class Interpreter:
  pass

class Token:
  pass

if __name__ == "__main__":
  print("Starting a python db session")
  session = start_session()
  print("Please enter an SQL command to execute")
  command = input()
  session.execute(command)
