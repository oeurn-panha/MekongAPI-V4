from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, Float
from database import Base

class Data(Base):
    __tablename__ = 'RiverData'
    
    id = Column(Integer, primary_key=True, index=True)
    RainGauge = Column(Float, index=True)
    FlowRate = Column(Float, index=True)
    Humidity = Column(Float, index=True)
    Temperature = Column(Float, index=True)
    WaterLevel = Column(Float, index=True )
    Station = Column(Integer, index=True)
    