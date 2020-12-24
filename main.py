from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/dynamic_routing/{number}")
async def return_number(number: int):  # type annotation syntax
    return {"number": number}
