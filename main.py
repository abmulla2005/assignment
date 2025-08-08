from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List
from fastapi.responses import JSONResponse
import models
import json
import schemas
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="🚆 ICF Forms API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if not os.path.exists("KPA_form_data.postman_collection.json.json"):
    with open("KPA_form_data.postman_collection.json.json", "w") as f:
        json.dump({}, f)

def load_data():
    try:
        with open("KPA_form_data.postman_collection.json.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

@app.get("/view")
def view_all_data():
    """View all patient records"""
    data = load_data()
    return data


@app.get("/api/forms/wheel-specifications", summary="Get all Wheel Specification forms")
def get_all_wheel_spec_forms(db: Session = Depends(get_db)):
    forms = db.query(models.WheelSpecificationsForm).all()
    return JSONResponse(content=[
        {
            "id": form.id,
            "formNumber": form.formNumber,
            "submittedBy": form.submittedBy,
            "submittedDate": str(form.submittedDate),
            "fields": form.fields
        }
        for form in forms
    ])

@app.get("/api/forms/bogie-checksheet", summary="Get all Bogie Checksheet forms")
def get_all_bogie_forms(db: Session = Depends(get_db)):
    forms = db.query(models.BogieChecksheetForm).all()
    return JSONResponse(content=[
        {
            "id": form.id,
            "formNumber": form.formNumber,
            "inspectionBy": form.inspectionBy,
            "inspectionDate": str(form.inspectionDate),
            "bogieDetails": form.bogieDetails,
            "bogieChecksheet": form.bogieChecksheet,
            "bmbcChecksheet": form.bmbcChecksheet
        }
        for form in forms
    ])


@app.post("/api/forms/wheel-specifications")
def submit_wheel_spec_form(form: schemas.WheelSpecificationsFormSchema, db: Session = Depends(get_db)):
    if db.query(models.WheelSpecificationsForm).filter_by(formNumber=form.formNumber).first():
        raise HTTPException(status_code=400, detail="Form number already exists")
    db_form = models.WheelSpecificationsForm(
        formNumber=form.formNumber,
        submittedBy=form.submittedBy,
        submittedDate=form.submittedDate,
        fields=form.fields.dict()
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return {"message": "Wheel Specification form submitted", "id": db_form.id}

@app.post("/api/forms/bogie-checksheet")
def submit_bogie_checksheet(form: schemas.BogieChecksheetFormSchema, db: Session = Depends(get_db)):
    if db.query(models.BogieChecksheetForm).filter_by(formNumber=form.formNumber).first():
        raise HTTPException(status_code=400, detail="Form number already exists")
    db_form = models.BogieChecksheetForm(
        formNumber=form.formNumber,
        inspectionBy=form.inspectionBy,
        inspectionDate=form.inspectionDate,
        bogieDetails=form.bogieDetails,
        bogieChecksheet=form.bogieChecksheet,
        bmbcChecksheet=form.bmbcChecksheet
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return {"message": "Bogie Checksheet form submitted", "id": db_form.id}
