from venSQL import BaseModel
from pydantic.dataclasses import dataclass

@dataclass
class Book(BaseModel):
    name: str
    lenght: int
    genre: str
    author_id: int
    table_name: str = "books"
