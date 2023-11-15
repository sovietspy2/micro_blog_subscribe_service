from typing import Annotated
from fastapi import Body, APIRouter
from pydantic import BaseModel, Field, EmailStr

router = APIRouter()

class Item(BaseModel):
    name: str | None = Field(default=None, title="The subscriber's name")
    time: int | None = Field(default=None, title="Time of the creation")
    email: EmailStr | None = None


@router.post("/subscriber")
async def update_item(subscriber: Annotated[Item, Body(embed=True)]):
    print(subscriber)
    return "hello"
