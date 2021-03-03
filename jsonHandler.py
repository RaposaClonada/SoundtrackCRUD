import importlib
json = importlib.import_module("json")

class JsonCRUD:
    def __init__(self, filename: str):
        filename = filename.split('.')[0]+'.json'
        try:
            file = open(filename)
            dictionary = json.loads(file.read())
            if not ('CRUD' in dictionary and len(dictionary) == 1 and type(dictionary['CRUD']) == list):
                raise FileNotFoundError
        except FileNotFoundError:
            file = open(filename, 'w')
            file.write(json.dumps({'CRUD': []}))
        file.close()
        self.filename = filename
        self.columns = ()
    
    def __len__(self):
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        return len(dictionary['CRUD'])
    
    def __getitem__(self, key):
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        return dictionary['CRUD'][key]
    
    def __delitem__(self, key):
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        del dictionary['CRUD'][key]
        dictionary = json.dumps(dictionary)
        file = open(self.filename, 'w')
        file.write(dictionary)
        file.close()

    def __iter__(self):
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        return (i for i in dictionary['CRUD'])
    
    def newColumn(self, columnName, *columnContents):
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        for itemIndex in range(len(self)):
            try:
                if type(columnContents[itemIndex]) not in (dict, list, tuple, str, float, int, bool, type(None)): raise IndexError
                dictionary['CRUD'][itemIndex][columnName] = columnContents[itemIndex]
            except IndexError:
                dictionary['CRUD'][itemIndex][columnName] = None
        file = open(self.filename, 'w')
        file.write(json.dumps(dictionary))
        file.close()