from venSQL import BaseModel, validate_fields

@validate_fields
class Author(BaseModel):
    table_name = "authors"
    id: int
    name: str
    age: int
