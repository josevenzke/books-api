import json

def deserializer(objects):
    return [obj.__dict__ for obj in objects]