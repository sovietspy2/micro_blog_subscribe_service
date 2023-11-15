from dotenv import load_dotenv

from fastapi import Body, FastAPI
from subscription.service import router

load_dotenv() 


app = FastAPI()

app.include_router(router)