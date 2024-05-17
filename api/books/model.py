from venSQL import BaseModel

class Book(BaseModel):
    table_name: str = "books"
    id: int
    name: str
    lenght: int
    genre: str
    author_id: int
