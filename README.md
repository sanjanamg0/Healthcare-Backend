# Healthcare Management Backend API

A Django-based REST API for managing patients, doctors, and their assignments using JWT authentication and PostgreSQL.

## 🚀 Getting Started

### 1. Set up Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
```bash
Create a .env file in the root directory and add your credentials (refer to .env.example):

SECRET_KEY

DATABASE_URL (PostgreSQL)
```

### 4. Database Migrations
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

### 🛠 API Endpoints
```bash
Authentication
POST /api/auth/register/ - Register a new user

POST /api/auth/login/ - Login and receive JWT tokens

Clinic Management (Requires JWT Token)
GET/POST /api/doctors/ - Manage doctor records

GET/POST /api/patients/ - Manage patients (User-specific)

GET/POST /api/mappings/ - Assign doctors to patients
```

### ✨ Features
```bash
JWT Security: All healthcare data endpoints are protected.

Data Isolation: Users can only see and manage patients they have personally created.

Cloud Database: Integrated with PostgreSQL for persistent storage.
```
