from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 全オリジンを許可するCORS設定
# ※開発都合上、全許可で設定しています。商用等では適切な設定にしてください。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのヘッダーを許可
)

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
