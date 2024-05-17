from typing import List
from venSQL import BaseModel

class Repository:
    def __init__(self):
        pass

    def get(self, model: BaseModel) -> List[object]:
        return model.objects.get_all()

    def get_one(self, model: BaseModel, id: int) -> object:
        return model.objects.get(id)
    
    def create(self, model: BaseModel, data: dict) -> object:
        return model.objects.create(data)
    
    def update(self, model: BaseModel, id: int, data: dict) -> object:
        return model.objects.update(id, data)
    
    def delete(self, model: BaseModel, id: int) -> bool:
        model.objects.delete(id)
        return True
