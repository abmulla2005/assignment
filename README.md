# 🚆 ICF Forms API

A FastAPI-based backend system for managing **Wheel Specifications** and **Bogie Checksheet** forms used in the railway (ICF) domain.

This project uses:
- ✅ FastAPI
- ✅ SQLAlchemy ORM
- ✅ SQLite (default DB)
- ✅ Pydantic for data validation
- ✅ JSON file fallback support for legacy data

---


4. Run the API server

uvicorn main:app --reload
📘 API Documentation
FastAPI automatically generates interactive docs:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

🛠 API Endpoints
🔍 View Raw JSON Data
Method	Endpoint	Description
GET	/view	View data from the KPA_form_data.postman_collection.json.json file

🧾 Wheel Specifications
Method	Endpoint	Description
GET	/api/forms/wheel-specifications	Fetch all Wheel Specification forms
POST	/api/forms/wheel-specifications	Submit a new Wheel Specification form

WheelSpecificationsForm Schema:

json

{
  "formNumber": "WS-001",
  "submittedBy": "Engineer Name",
  "submittedDate": "2025-08-08",
  "fields": {
    "wheelDiameter": "840mm",
    "treadWear": "10mm"
  }
}
🧾 Bogie Checksheet

GET	/api/forms/bogie-checksheet	Fetch all Bogie Checksheet forms
POST	/api/forms/bogie-checksheet	Submit a new Bogie Checksheet form

BogieChecksheetForm Schema:

json
Copy
Edit
{
  "formNumber": "BC-001",
  "inspectionBy": "Inspector Name",
  "inspectionDate": "2025-08-08",
  "bogieDetails": "Bogie Type XYZ",
  "bogieChecksheet": "All checks passed",
  "bmbcChecksheet": "Brake checks passed"
}
📁 Project Structure
pgsql
Copy
Edit
.
├── main.py                          # FastAPI application entry
├── models.py                        # SQLAlchemy models
├── schemas.py                       # Pydantic schemas
├── database.py                      # Database session setup
├── KPA_form_data.postman_collection.json.json  # JSON file for fallback/raw data
├── requirements.txt
└── README.md
✅ Future Improvements
Add authentication and role-based access control.

Pagination for GET endpoints.

Input validation on nested fields.

Integration with a frontend (e.g., Flutter or React).

Unit and integration tests.

👨‍💻 Author
Abrar Mulla
📧 abmulla2005@gmail.com
🔗 www.linkedin.com/in/abrar-mulla-326778306


