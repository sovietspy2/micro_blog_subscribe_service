from dotenv import load_dotenv

from fastapi import Body, FastAPI
from .subscription.service import router
import logging 
logging.basicConfig(level=logging.INFO)

load_dotenv() 


app = FastAPI()

app.include_router(router)