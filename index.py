class Index:
    def __init__(self, table, field):
        self.table = table
        self.field = field
        self.hash = {}
        for entry in self.field:
            self.hash.update({entry: location})