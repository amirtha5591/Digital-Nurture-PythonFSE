# Hands-On 07 – FastAPI CRUD Operations with SQLAlchemy

## 📖 Overview

This hands-on focuses on developing RESTful APIs using FastAPI and SQLAlchemy. The project demonstrates how to create a backend application that performs database operations using SQLite while validating request and response data with Pydantic schemas.

The application follows a modular architecture where database configuration, models, schemas, and API routes are organized into separate files for improved readability and maintainability.

---

# 🎯 Objectives

- Build REST APIs using FastAPI.
- Integrate SQLAlchemy ORM with FastAPI.
- Perform CRUD (Create, Read, Update, Delete) operations.
- Validate API requests using Pydantic.
- Connect the application with SQLite database.
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
handson_07/
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── college.db
├── requirements.txt
└── README.md
```

---

# 🚀 Features Implemented

- FastAPI Application Setup
- SQLite Database Integration
- SQLAlchemy ORM
- Pydantic Schema Validation
- CRUD API Endpoints
- Modular Project Structure
- Interactive Swagger Documentation

---

# 📚 Key Concepts Covered

## FastAPI

FastAPI is a high-performance Python web framework used to develop RESTful APIs with automatic validation and interactive documentation.

---

## SQLAlchemy ORM

SQLAlchemy provides Object Relational Mapping (ORM) that allows developers to interact with relational databases using Python classes.

Implemented features include:

- Database connection
- Model creation
- CRUD operations
- Session management

---

## Pydantic Schemas

Pydantic models validate incoming request data and serialize API responses.

Benefits include:

- Automatic validation
- Data serialization
- Type checking
- Error reporting

---

## SQLite Database

SQLite is used as the backend relational database for storing application records during development.

---

## Modular Architecture

The project separates application components into different modules.

- **database.py** – Database configuration and connection
- **models.py** – SQLAlchemy database models
- **schemas.py** – Pydantic request and response schemas
- **main.py** – FastAPI application and API endpoints

---

# ⚙ Installation

Clone the repository.

Install dependencies.

```bash
pip install -r requirements.txt
```

Start the FastAPI server.

```bash
uvicorn main:app --reload
```

Open the application:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

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
| college.db | SQLite database |
| requirements.txt | Project dependencies |

---

# 📖 Learning Outcomes

After completing this hands-on, I learned:

- Building REST APIs using FastAPI
- Implementing CRUD operations
- Integrating SQLAlchemy ORM
- Managing SQLite databases
- Validating data using Pydantic
- Organizing FastAPI applications using modular architecture
- Testing APIs using Swagger UI

---

# 🔮 Future Enhancements

- JWT Authentication
- User Authorization
- Pagination
- Search & Filtering
- Exception Handling
- API Versioning
- Unit Testing
- Docker Deployment

---

# ✅ Conclusion

This hands-on provided practical experience in developing RESTful APIs using FastAPI and SQLAlchemy. It demonstrated how to organize backend applications using modular architecture while implementing CRUD operations, request validation, database connectivity, and automatic API documentation. The knowledge gained from this exercise forms a strong foundation for building scalable backend web services.
