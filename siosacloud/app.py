import sys
import os
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from api import router
from fastapi.middleware.cors import CORSMiddleware

from db.mongo import connect_db, close_db

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

app.add_event_handler('startup', connect_db)
app.add_event_handler('shutdown', close_db)