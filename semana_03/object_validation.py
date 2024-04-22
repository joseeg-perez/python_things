from pydantic import ValidationError
from typing import TypeVar

T = TypeVar("T")
E = TypeVar("E")

def validate_object(class_: T, object: E):
    #Pasando un diccionario para crear una instancia
    try:
        response = class_(**object)
    except ValidationError as e: 
        print(e.errors())
    
    return response