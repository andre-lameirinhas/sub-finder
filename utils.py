import json

def print_json(content):
    print(json.dumps(dict(content), indent = 3))
    