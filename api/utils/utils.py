from typing import Union
from venSQL.model import BaseModel

def deserializer(objects: Union[BaseModel,list[BaseModel]], many=False) -> list:
    if many:
        return [obj.__dict__ for obj in objects]
    return objects.__dict__