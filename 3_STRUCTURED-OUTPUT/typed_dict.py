from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'Krishna', 'age': '23'}  # even if age is str and not int, the code will still run
print(new_person)