from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    num1: int
    num2: int
    operator: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/calc")
async def calc(num1, operator, num2):
    answer = 0
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    return {answer}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info")
