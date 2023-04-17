
def deserializer(objects: list) -> list:
    return [obj.__dict__ for obj in objects]