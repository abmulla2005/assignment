from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from database import Base

class WheelSpecificationsForm(Base):
    __tablename__ = "wheel_specifications"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)

class BogieChecksheetForm(Base):
    __tablename__ = "bogie_checksheet"
    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True)
    inspectionBy = Column(String)
    inspectionDate = Column(Date)
    bogieDetails = Column(JSON)
    bogieChecksheet = Column(JSON)
    bmbcChecksheet = Column(JSON)
