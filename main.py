from fastapi import FastAPI
import etl_work

app = FastAPI()

@app.get("/")
async def root():
    return etl_work.hello_word_print_from_etl()