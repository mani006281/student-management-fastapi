# 🎓 Student Management System — FastAPI + JWT Authentication

A full-stack **Student Management System** built using **FastAPI**, **PostgreSQL**, and **JWT Authentication**. This project provides secure REST APIs for managing student records with role-based authorization, ensuring that only the creator of a student record can edit or delete it.

The application includes a simple HTML/CSS/JavaScript frontend and is deployed on **Render** with a PostgreSQL database.

---

# 🚀 Live Demo

### 🌐 Application

https://student-management-fastapi-1-ca4z.onrender.com

### 📖 Swagger API Documentation

https://student-management-fastapi-1-ca4z.onrender.com/docs

---

# ✨ Features

- User Registration
- Secure User Login using JWT Authentication
- Password Hashing with Passlib (bcrypt)
- Create Student Records
- View Student Records
- Update Student Records
- Delete Student Records
- Search Students
- Ownership-Based Authorization
- PostgreSQL Database Integration
- Interactive Swagger UI
- RESTful API Design

---

# 🔐 Authentication & Authorization

The project implements JWT (JSON Web Token) authentication.

### Authentication

- Register a new user
- Login securely
- Generate JWT Access Token
- Access protected endpoints

### Authorization

Only the authenticated user who created a student record can:

- ✏️ Edit the student
- 🗑️ Delete the student

Other users can view the student record but will see:

```
No Permission
```

This demonstrates ownership-based access control.

---

# 🛠 Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Passlib (bcrypt)
- **Validation:** Pydantic
- **ASGI Server:** Uvicorn
- **Deployment:** Render

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register User |
| POST | `/auth/login` | Login User |

---

## Students

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get All Students |
| GET | `/students/{id}` | Get Student by ID |
| POST | `/students` | Create Student |
| PUT | `/students/{id}` | Update Student |
| DELETE | `/students/{id}` | Delete Student |

---

# 📥 Example Login Request

```bash
curl -X POST https://student-management-fastapi-1-ca4z.onrender.com/auth/login \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=Prakash&password=yourpassword"
```

---

# 📤 Example Response

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
    "token_type": "bearer"
}
```

---

# ▶️ Getting Started

```bash
# Clone repository
git clone https://github.com/mani006281/student-management-fastapi.git

# Navigate into project
cd student-management-fastapi

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

# 📂 Project Structure

```
student-management-fastapi
│
├── app
│   ├── routes
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── frontend
│   ├── index.html
│   └── dashboard.html
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing (bcrypt)
- Protected API Routes
- Ownership-Based Authorization
- Secure Password Storage

---

# 🌟 Future Improvements

- Admin Dashboard
- User Roles (Admin/Faculty/Student)
- Student Profile Images
- Pagination
- Email Verification
- Password Reset
- Docker Support
- CI/CD Pipeline

---

# 👨‍💻 Developer

**Mani Kumar Penugonda**

- GitHub: https://github.com/mani006281
- LinkedIn: https://www.linkedin.com/in/mani-kumar-penugonda-096705363

---

⭐ If you found this project useful, don't forget to star the repository!