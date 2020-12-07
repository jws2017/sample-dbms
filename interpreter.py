class Session:
  def __init__(self):
    self.id = 0
    self.databases = []
    self.database_names = []
    self.current = None
  def create_database(self, name):
    if name in self.database_names: raise Exception("Database %s already exists".format(name))
    db = Database(name)
    self.databases.append(db)
    self.database_names.append(name)
    return db
  def clear_current(self):
    if self.current is not None:
      self.current = None
  def set_current(self, db):
    if db not in self.databases:
      raise Exception("Database %s does not exist".format(db.name))
    elif db == self.current:
      print("%s is already the current database".format(db.name))
    else:
      self.current = db
      print("%s is now the current database".format(db.name))

class Database:
  def __init__(self, name):
    self.name = name
  def create_table(name, column_dict):
    pass
  def drop_table(name):
    pass

class Table:
  pass

if __name__ == "__main__":
  pass
