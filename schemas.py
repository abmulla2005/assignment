from pydantic import BaseModel
from typing import Dict
from datetime import date

class WheelSpecFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecificationsFormSchema(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelSpecFields

class BogieChecksheetFormSchema(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: Dict[str, str]
    bogieChecksheet: Dict[str, str]
    bmbcChecksheet: Dict[str, str]
