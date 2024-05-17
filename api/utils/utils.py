from typing import Union, List
from venSQL.model import BaseModel

def deserializer(objects: Union[BaseModel,List[BaseModel]], many=False) -> list:
    if many:
        return [obj.__dict__ for obj in objects]
    return objects.__dict__