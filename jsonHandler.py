import importlib
json = importlib.import_module("json")

class JsonCRUD:
    def __init__(self, filename: str):
        filename = filename.split('.')[0]+'.json'
        try:
            file = open(filename)
            dictionary = json.loads(file.read())
            if not ('CRUD' in dictionary and 'columns' in dictionary and len(dictionary) == 2 and type(dictionary['CRUD']) == list):
                raise FileNotFoundError
        except FileNotFoundError:
            file = open(filename, 'w')
            file.write(json.dumps({'columns': [],'CRUD': []}))
            dictionary = {'columns': [],'CRUD': []}
        self.columns = tuple(dictionary['columns'])
        file.close()
        self.filename = filename
    
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
        dictionary['columns'] += [columnName]
        file = open(self.filename, 'w')
        file.write(json.dumps(dictionary))
        file.close()
        self.columns += tuple([columnName])
    
    def newItem(self, *columnsContent):
        item = {}
        for index in range(len(self.columns)):
            try:
                if type(columnsContent[index]) not in (dict, list, tuple, str, float, int, bool, type(None)): raise IndexError
                item[self.columns[index]] = columnsContent[index]
            except IndexError:
                item[self.columns[index]] = None
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        dictionary['CRUD'].append(item)
        file = open(self.filename, 'w')
        file.write(json.dumps(dictionary))
        file.close()
    
    def delColumn(self, column):
        columns = list(self.columns)
        columns.remove(column)
        self.columns = tuple(columns)
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        del dictionary['columns'][dictionary['columns'].index(column)]
        for item in dictionary['CRUD']:
            del item[column]
        file = open(self.filename, 'w')
        file.write(json.dumps(dictionary))
        file.close()
    
    def updateItem(self, index, column, value):
        file = open(self.filename)
        dictionary = json.loads(file.read())
        file.close()
        if column not in dictionary['columns']: raise KeyError
        if type(value) not in (dict, list, tuple, str, float, int, bool, type(None)): value = None
        dictionary['CRUD'][index][column] = value
        file = open(self.filename, 'w')
        file.write(json.dumps(dictionary))
        file.close()