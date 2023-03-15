import json


def read_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data


def write_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

