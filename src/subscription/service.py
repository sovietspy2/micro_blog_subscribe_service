from typing import Annotated, ItemsView
from fastapi import Body, APIRouter
from pydantic import BaseModel, Field, EmailStr
import logging

router = APIRouter()

class Item(BaseModel):
    name: str | None = Field(default=None, title="The subscriber's name")
    time: int | None = Field(default=None, title="Time of the creation")
    email: EmailStr | None = None


@router.post("/subscription")
async def subscribe(subscriber: Item):
    logging.debug(subscriber.model_dump_json())
    return "ok"
