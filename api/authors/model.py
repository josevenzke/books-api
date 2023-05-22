from venSQL import BaseModel, validate_fields
from utils.constants import DB_SETTINGS

@validate_fields
class Author(BaseModel):
    table_name = "authors"
    id: int
    name: str
    age: int
