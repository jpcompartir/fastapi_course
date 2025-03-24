class Person:
    def __init__(self, name):
        self.name = name

def get_one_person(one_person: Person):
    return one_person.

from datetime import datetime
from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    name: str = "Jimmy Riddle"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user1 = User(**external_data)

print(user1.model_dump_json(indent = 2))


from typing import Annotated

def say_hello(name: Annotated[str, "Enter full name here separated by a space"]) -> str:
    return f"Hello {name}"

