
from fastapi import FastAPI
from pydantic import BaseModel

myapi = FastAPI(title="Simple API")

class Numbers(BaseModel):
    a: float
    b: float

@myapi.get("/")
def home():
    return {"message": "Hello, this is me!"}

@myapi.post("/add")
def add_numbers(nums: Numbers):
    return {"a": nums.a, "b": nums.b, "result": nums.a + nums.b}


@myapi.get("/msg")
def home():
    return {"message": "Trying to run FastAPI on WSL!"}

@myapi.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hi {name}, welcome to my API!"}