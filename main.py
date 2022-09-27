from fastapi import FastAPI

import uvicorn

app = FastAPI()

#get, put, delete,

#get
@app.get("/")
async def hello_world():
    return {"hello : world"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

