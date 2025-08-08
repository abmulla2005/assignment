# 🚆 ICF Forms API

A FastAPI-based backend system for managing **Wheel Specifications** and **Bogie Checksheet** forms used in the railway (ICF) domain.

This project uses:
- ✅ FastAPI
- ✅ SQLAlchemy ORM
- ✅ SQLite (default DB)
- ✅ Pydantic for data validation
- ✅ JSON file fallback support for legacy data

---

## 📦 Features

- Submit and fetch **Wheel Specifications** forms.
- Submit and fetch **Bogie Checksheet** forms.
- Automatically prevents duplicate form submissions based on `formNumber`.
- Supports JSON-based backup loading from `KPA_form_data.postman_collection.json.json`.
- Clean and structured API responses via FastAPI + JSONResponse.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/icf-forms-api.git
cd icf-forms-api
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
requirements.txt Example:

nginx
Copy
Edit
fastapi
uvicorn
sqlalchemy
pydantic
4. Run the API server
bash
Copy
Edit
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
Copy
Edit
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
Method	Endpoint	Description
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
📧 [Your Email]
🔗 [Your LinkedIn / GitHub Profile]

📝 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---



