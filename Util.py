import json
# read json from file

def read_from_file(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
        return data
