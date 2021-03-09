import importlib

JsonCRUD = importlib.import_module("jsonHandler").JsonCRUD
time = importlib.import_module("time")

class soundtrackCRUD(JsonCRUD):
    def __init__(self, filename):
        super().__init__(filename)
        self.newColumn('Name')
        self.newColumn('Date of Creation')
        self.newColumn('Tags')
    
    def newSoundtrack(self, name: str):
        self.newItem(name, time.time(), [])
    
    def addTag(self, index: int, tag: str):
        tags = self[index]['Tags']
        tags.append(tag)
        self.updateItem(index, 'Tags', tags)
    
    def removeTag(self, index: int, tag: str):
        tags = self[index]['Tags']
        tags.remove(tag)
        self.updateItem(index, 'Tags', tags)