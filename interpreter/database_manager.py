"""This module defines the DatabaseManager class, which acts as an intermediary between the database and the application. The application calls the methods of a database manager to conduct operations."""
import dataclasses

class DatabaseManager:
    """An intermediary between the application interface and the database itself."""
    def __init__(self, *args, **kwargs):
        self._databases = {}
        self.current_database = None
        super().__init__(*args, **kwargs)

    def create_database(self, name):
        """Creates a database object, an abstract representation of a database"""
        if name in self._databases:
            raise Exception("Database already exists")
        database = Database(name, tables = [])
        self._databases[name] = database

    def delete_database(self, name):
        if name not in self._databases:
            raise Exception("Database does not exist")
        if self.current_database is not None and self.current_database.name == name:
            self.current_database = None
        del self._databases[name]

    def use_database(self, name):
        if name not in self._databases:
            raise Exception("Database not created")
        self.current_database = self._databases[name]

    def databases(self):
        return self._databases.values()

    def create_table(self, name):
        if self.current_database is None:
            raise Exception("Database not selected")
        new_table = Table(name)
        self.current_database.tables[name] = new_table
        return

    def delete_table(self, name):
        if self.current_database is None:
            raise Exception("Database not selected")
        if name not in self.current_database.tables:
            raise Exception("Table not found")
        del self.current_database.tables[name]


@dataclasses.dataclass
class Database:
    name: str
    tables: dict({str: Table})

@dataclasses.dataclass
class Table:
    name: str
