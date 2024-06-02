import json

def write_json(data, file_path, pretty=False):
    with open(file_path, mode='w', encoding='utf-8') as jsonfile:
        if pretty:
            json.dump(data, jsonfile, indent=4)
        else:
            json.dump(data, jsonfile)
