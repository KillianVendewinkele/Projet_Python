from fastapi import FastAPI

import uvicorn

app = FastAPI()


# get, put, delete,

# get
@app.get("/")
async def hello_world():
    return {"hello : world"}


@app.get("/component/{}component_id")  # path parameter
async def get_component(component_id: int):
    # operation
    return {"component_id": component_id}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
