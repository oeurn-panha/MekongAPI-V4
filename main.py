from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel #data validation
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import desc
import random
from randomnumber import RandNumber

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class RiverData(BaseModel):
    RainGauge: float
    PH: float
    Humidity: float
    Temperature: float
    WaterLevel: float
    
#==================================================================================================#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()      
#==================================================================================================#
db_dependancy = Annotated[Session, Depends(get_db)]
#==================================================================================================#
stationOne = 1
#==================================================================================================#
# RandNumber.Random()
#==================================================================================================#
@app.post('/riverdata/')
async def Send_River_Data(RiverData: RiverData, db: db_dependancy):
    db_data = models.Data(
        RainGauge = RiverData.RainGauge,
        PH = RiverData.PH,
        Temperature = RiverData.Temperature,
        Humidity = RiverData.Humidity,
        WaterLevel = RiverData.WaterLevel,
        Station = stationOne
        )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    
@app.get('/riverdata')
async def Read_River_Data(db:db_dependancy):
    
    # ===========================================================#
    db_data = models.Data(
        PH = random.randrange(1, 800)/8,
        RainGauge = random.randrange(1, 400)/4,
        Humidity = random.randrange(1, 400)/4,
        Temperature = random.randrange(1, 400)/4,
        WaterLevel = random.randrange(1, 400)/4,
        Station = stationOne
        )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    # ===========================================================#
    result = db.query(models.Data).order_by(desc(models.Data.id)).first()
    if not result:
        raise HTTPException(status_code=404, detail="database is not found.")
    return result
    
