from fastapi import FastAPI
from src.math_operations import add, sub

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI CI/CD Demo"}

@app.get("/add")
def add_numbers(a: int, b: int):
    result = add(a, b)
    return {"result": result}

@app.get("/sub")
def sub_numbers(a: int, b: int):
    result = sub(a, b)
    return {"result": result}