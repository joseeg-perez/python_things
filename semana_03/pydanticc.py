from pydantic import BaseModel, Field
from typing import List
from object_validation import validate_object

#Hay que extender de la clase BaseModel
class User(BaseModel):
    name: str = Field(min_length=1)
    email: str
    account_id: int
    followers: List[str] = []

#Para instanciar un objeto
jose = User(name="jose", email="jose@gmail.com", account_id=123, followers=["Luis", "Maria"])

#Objeto con estructura de instancia de tipo usuario
frontend_response = {
    "name": "maria",
    "email": "maria@gmail.com",
    "account_id": 234,
    "followers": ["juan", "julio"],
}


#Funcion que valida un usuario
maria = validate_object(User, frontend_response)
print(maria)


from enum import Enum

class Languages(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "go"

class Blog(BaseModel):
    title: str
    language: Languages
    is_active: bool


blog_jose = Blog(title="Un dia en la uni", language="python", is_active=True)
#Para pasar a JSON
print(blog_jose.model_dump_json())

#Da error porque TypeScript no es un valor valido para el enum
# blog_jose_malo = Blog(title="Un dia en la uni", language="TypeScript", is_active=True)