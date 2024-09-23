import random
import models
import time
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from database import engine, SessionLocal
# ==================================================================================#
models.Base.metadata.create_all(bind=engine)
# ==================================================================================#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()      
#====================================================================================#
db_dependancy = Annotated[Session, Depends(get_db)]
#====================================================================================#

stationOne = 1
class RandNumber():
    async def Random():
        while True:
            db:db_dependancy
            db_data = models.Data(
            TotDissSens = random.randrange(1, 400)/4.9,
            DissOxySens = random.randrange(1, 400)/4,
            TempCSens = random.randrange(1, 400)/4,
            PHSens = random.randrange(1, 400)/4,
            WaterLevSens = random.randrange(1, 400)/4,
            Station = stationOne
            )
            db.add(db_data)
            db.commit()
            db.refresh(db_data)
            time.sleep(1)