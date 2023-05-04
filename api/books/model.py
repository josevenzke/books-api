from venSQL import BaseModel
from pydantic.dataclasses import dataclass

class Book(BaseModel):
    id: int
    name: str
    lenght: int
    genre: str
    author_id: int
    table_name: str = "books"
