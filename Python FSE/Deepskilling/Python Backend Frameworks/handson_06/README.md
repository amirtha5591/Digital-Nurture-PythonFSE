# Hands-On 06 – FastAPI with SQLAlchemy Database Integration

## 📖 Overview

This hands-on introduces backend API development using **FastAPI**, a modern high-performance Python web framework. The project demonstrates how to integrate FastAPI with SQLAlchemy ORM, create database models, define request and response schemas using Pydantic, and build a structured REST API application.

The application follows a modular architecture where database configuration, models, schemas, and API endpoints are separated into different files for better maintainability.

---

# 🎯 Objectives

- Understand FastAPI fundamentals.
- Build RESTful APIs using FastAPI.
- Integrate SQLAlchemy ORM.
- Create SQLite database models.
- Use Pydantic schemas for request validation.
- Organize backend applications using modular architecture.

---

# 🛠 Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn
- VS Code

---

# 📂 Project Structure

```
handson_06/
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── courses.db
├── requirements.txt
└── README.md
```

---

# 🚀 Features Implemented

- FastAPI Application Setup
- SQLAlchemy Database Integration
- SQLite Database
- Pydantic Request Validation
- Database Models
- REST API Endpoints
- Modular Project Structure
- Automatic API Documentation

---

# 📚 Key Concepts Covered

## FastAPI

FastAPI is a modern Python framework used to build high-performance REST APIs with automatic validation and interactive API documentation.

---

## SQLAlchemy ORM

SQLAlchemy is used to map Python classes to database tables and perform database operations without writing raw SQL queries.

---

## Pydantic Schemas

Pydantic models validate incoming request data and serialize responses automatically.

Benefits include:

- Input validation
- Type checking
- JSON serialization
- Error handling

---

## SQLite Database

SQLite is used as the backend database for storing application records during development.

---

## Modular Architecture

The project is organized into separate modules.

- **database.py** – Database connection and session management
- **models.py** – SQLAlchemy models
- **schemas.py** – Pydantic schemas
- **main.py** – FastAPI application and API endpoints

---

# ⚙ Installation

Clone the repository.

Install project dependencies.

```bash
pip install -r requirements.txt
```

Start the FastAPI development server.

```bash
uvicorn main:app --reload
```

Open the application in your browser.

```
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

Alternative API documentation:

```
http://127.0.0.1:8000/redoc
```

---

# 📁 Important Files

| File | Description |
|------|-------------|
| main.py | FastAPI application entry point |
| database.py | Database configuration |
| models.py | SQLAlchemy models |
| schemas.py | Pydantic schemas |
| courses.db | SQLite database |
| requirements.txt | Project dependencies |

---

# 📖 Learning Outcomes

After completing this hands-on, I learned:

- FastAPI application development
- REST API creation
- SQLAlchemy ORM integration
- SQLite database management
- Request validation using Pydantic
- API documentation using Swagger UI
- Modular backend project organization

---

# 🔮 Future Enhancements

- Complete CRUD Operations
- JWT Authentication
- User Authorization
- Pagination
- Search & Filtering
- Exception Handling
- API Versioning
- Docker Deployment

---

# ✅ Conclusion

This hands-on provided practical experience in developing REST APIs using FastAPI with SQLAlchemy. It demonstrated how to organize backend applications using modular architecture while implementing database connectivity, request validation, and automatic API documentation. The concepts learned here form a strong foundation for building scalable backend web services.
