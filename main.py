from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/yolo")
async def yolo():
    return {"message": "You only live once !"}
