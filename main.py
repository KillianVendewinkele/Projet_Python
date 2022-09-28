from fastapi import FastAPI

import uvicorn

app = FastAPI()

# get, put, delete,

# get
@app.get("/")
async def hello_world():
    return {"hello : world"}


@app.get("/component/{}client_id")  # path parameter
async def get_client(client_id: int):
    # operation
    return {"client_id": client_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
