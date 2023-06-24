from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Te amo mucho Angelica :3 **japy japy jaaapy, japyjapyjapyjapy:3 "}