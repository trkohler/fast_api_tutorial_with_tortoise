from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/dynamic_routing/{number}")
async def return_number(number: int, add: int = 0, multiply: int = 1):
    return {"number": (number + add) * multiply}
