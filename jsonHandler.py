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
    
a = JsonCRUD('arquivo')