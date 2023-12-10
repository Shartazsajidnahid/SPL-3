from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

class DayofWeekInfo(BaseModel):

    typename: str
    occurrence: int = 0
    dead: int = 0
    injured: int = 0
