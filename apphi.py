
from fastapi import FastAPI

myapi = FastAPI()

@myapi.get("/")
def home():
    return {"message": "Hello, this is me!"}

@myapi.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@myapi.get("/msg")
def home():
    return {"message": "Trying to run FastAPI on WSL!"}

@myapi.get("/greet/{name}")
def greet(name: str):
    return {"greeting": f"Hi {name}, welcome to my API!"}