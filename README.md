# 🗓️ Event Management API

A RESTful backend built with **FastAPI** that allows users to create, manage, and collaborate on events with full role-based permissions, versioning, and changelog diffing.

## 🚀 Features

✅ Token-based authentication (JWT)  
✅ Role-based access control (Owner, Editor, Viewer)  
✅ Full CRUD for events  
✅ Recurring events support  
✅ Versioning with rollback and diff  
✅ Share events with users and assign roles  
✅ OpenAPI/Swagger docs (`/docs`)  
✅ Lightweight & deployable via Hugging Face Spaces

---

## 📦 Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **SQLite** (easy to swap with PostgreSQL)
- **Pydantic v2**
- **JWT** for secure token-based authentication

---

## 🧑‍💻 Installation (Local)

```bash
git clone https://github.com/your-username/neofi-backend-api.git
cd neofi-backend-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload

🚧 API Endpoints
🧾 Auth
Method	Endpoint	Description
POST	/api/auth/register	Register new user
POST	/api/auth/login	Get JWT token
POST	/api/auth/refresh	Refresh token (if enabled)

📅 Events
Method	Endpoint	Description
POST	/api/events	Create new event
GET	/api/events	List accessible events
GET	/api/events/{id}	Get event by ID
PUT	/api/events/{id}	Update event
DELETE	/api/events/{id}	Delete event
POST	/api/events/batch	Batch create events

👥 Collaboration
Method	Endpoint	Description
POST	/api/events/{id}/share	Share with users + roles
GET	/api/events/{id}/permissions	View current permissions
PUT	/api/events/{id}/permissions/{userId}	Change a user's role
DELETE	/api/events/{id}/permissions/{userId}	Revoke access

🕓 Versioning & Changelog
Method	Endpoint	Description
GET	/api/events/{id}/versions	Get all versions
GET	/api/events/{id}/history/{versionId}	Get specific version
POST	/api/events/{id}/rollback/{versionId}	Roll back to version
GET	/api/events/{id}/diff/{v1}/{v2}	Field-by-field dif


https://github.com/Tejas1020/Rest_API_Management/blob/main/registration.png
![API Screenshot][(https://via.placeholder.com/900x500.png](https://github.com/Tejas1020/Rest_API_Management/blob/main/registration.png)?text=NeoFi+Backend+API+Swagger+UI)
