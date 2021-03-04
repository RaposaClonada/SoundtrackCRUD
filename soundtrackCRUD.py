import importlib

JsonCRUD = importlib.import_module("jsonHandler").JsonCRUD

class soundtrackCRUD(JsonCRUD):
    def __init__(self, filename):
        super().__init__(filename)
        self.newColumn('Name')
        self.newColumn('Date of Creation')
        self.newColumn('Tags')