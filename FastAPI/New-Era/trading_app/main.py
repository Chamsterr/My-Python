from fastapi import FastAPI
from dataclasses import dataclass

app = FastAPI()

@app.get("/")
def get_hello():
    return "hello"

list_of_smth: list[int|str] = [1, 2, 3, 4, "cat"]

@app.get("/number/{id}")
def get_number_with_id_in_url(id: int) -> int|str:
    return list_of_smth[id]

@app.get("/number/")
def get_number_with_parametr(id: int = 0) -> int|str:
    return list_of_smth[id]

@dataclass
class User:
    id: int
    name: str

users: list[User] = [
    User(id = 1, name ="James"),
    User(id = 2, name="Jamal")
]

@app.patch("/change_name/{user_id}")
def change_name_by_id(user_id: int, new_name: str):
    user = next(user_ for user_ in users if user_.id == user_id)
    user.name = new_name
    return {"status": 200, "data": user}