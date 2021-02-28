import importlib
json = importlib.import_module("json")

class JsonCRUD:
    def __init__(self, file):
        self.file = file
        self.columns = ()
        self.num_itens = 0
    
    def newColumn(self, column_name: str):
        with open(self.file) as file:
            dictionary = json.load(file)
            for itens in dictionary:
                dictionary[itens][column_name] = 'N\A'
            json.dump(dictionary, file)
        self.columns += tuple([column_name])
    
    def addNewItem(self):
        with open(self.file) as file:
            dictionary = json.load(file)
            dictionary[self.num_itens] = {}
            self.num_itens += 1
            for columns in self.columns:
                dictionary[self.num_itens-1][columns] = 'N\A'
            json.dump(dictionary, file)
    
    def editItem(self, index, column, data):
        with open(self.file) as file:
            dictionary = json.load(file)
            dictionary[str(index)][column] = data
            json.dump(dictionary, file)
    
    def removeItem(self, index):
        with open(self.file) as file:
            dictionary = json.load(file)
            for i in dictionary:
                if int(i) <= int(index): continue
                dictionary[str(int(i)-1)] = dictionary[i]
            del dictionary[i]
            json.dump(dictionary, file)
        self.num_itens -= 1
    
    def removeColumn(self, column):
        with open(self.file) as file:
            dictionary = json.load(file)
            for i in dictionary:
                del dictionary[i][column]
            json.dump(dictionary, file)
        temporary_list = list(self.columns)
        temporary_list.remove(column)
        self.columns = tuple(temporary_list)
    
    def returnItem(self, index):
        with open(self.file) as file:
            dictionary = json.load(file)
            return dictionary[str(index)]