
##############################################################################

from fastapi import FastAPI

from routes.movies import movies


app = FastAPI()

app.include_router(movies)







