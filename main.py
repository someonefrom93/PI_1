from fastapi import FastAPI
import etl_work

app = FastAPI()

@app.get("/")
def root():
    return etl_work.first_endpoint()