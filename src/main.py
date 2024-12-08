from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    num1: object
    num2: object
    operator: object


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/calc")
async def calc(num1, operator, num2):
    answer = 0
    i_num1 = int(num1)
    i_num2 = int(num2)
    str_operator = str(operator)


    if str_operator == '+':
        answer = i_num1 + i_num2
    elif str_operator == '-':
        answer = i_num1 - i_num2
    elif str_operator == '*':
        answer = i_num1 * i_num2
    elif str_operator == '/':
        answer = i_num1 / i_num2
    return {answer}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info")
