from venSQL import BaseModel

class Book(BaseModel):
    id: int
    name: str
    lenght: int
    genre: str
    author_id: int
    table_name: str = "books"
