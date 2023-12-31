from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "My REST API server!"}