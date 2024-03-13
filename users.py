import json

def save_ids(filename, id_list):
    with open(filename, 'w') as file:
        json.dump(id_list, file)

def load_ids(filename):
    with open(filename, 'r') as file:
        id_list = json.load(file)
        return id_list
    
