from venSQL import BaseModel

class Book(BaseModel):
    table_name: str = "books"
    name: str
    lenght: int
    genre: str
    author_id: int
