x: str = 1

def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

from typing import List, Dict, Set
x: List[List[int]] = [[1,2], [3,4]] #Para verificar una lista de enteros dentro de otra lista

x: Dict[str, str] = {"a": "b"} #Para verificar que la clave y el valor de un diccionario son los mismos

x: Set[str] = {"a", "b"} #Para verificar que el par es de un tipo particular

#Custom types
Vector = List[float]

def foo(v: Vector) -> Vector:
    return v

Vectors = List[Vector] #Lista que contiene una lista de floats pero se llama Vector

#Sobrecarga de metodos
def foo(v: Vectors) -> Vector:
    return v[0]

print( foo([[1.4, 1.5], [1.0, 2.0]]) )