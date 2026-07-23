# Hands-On 03 – Django REST Framework API Development

## 📖 Overview

This hands-on focuses on building RESTful APIs using Django and Django REST Framework (DRF). The project demonstrates how to create models, serialize data, develop API views, and expose REST endpoints for a University Management System.

The application uses Django ORM with SQLite as the backend database and provides APIs to manage university-related information.

---

# 🎯 Objectives

- Learn the fundamentals of Django REST Framework.
- Build REST APIs using Django.
- Understand Serializers and API Views.
- Connect Django models with REST endpoints.
- Store data using SQLite.
- Test APIs using a web browser or API testing tools.

---

# 🛠 Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite3
- VS Code

---

# 📂 Project Structure

```
handson_03/
│
├── coursemanager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── university/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   └── migrations/
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Features Implemented

- Django Project Configuration
- Django REST Framework Integration
- University Application
- Database Models
- Serializers
- API Views
- URL Routing
- SQLite Database
- Migration Support

---

# 📚 Key Concepts Covered

## Django REST Framework

Django REST Framework simplifies the development of RESTful web services by providing tools for serialization, request handling, authentication, and API responses.

---

## Models

Models define the database structure using Python classes.

Example entities include university-related records managed through Django ORM.

---

## Serializers

Serializers convert Django model objects into JSON format and validate incoming request data before storing it in the database.

---

## Views

Views process client requests and return JSON responses through REST APIs.

---

## Database

SQLite is used as the default database for storing application data during development.

---

# ⚙ Installation

Clone the repository.

Install dependencies.

```bash
pip install -r requirements.txt
```

Apply migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the development server.

```bash
python manage.py runserver
```

---

# 🌐 API Access

After starting the server, APIs can be accessed at:

```
http://127.0.0.1:8000/
```

Depending on the configured URLs, endpoints can be tested using:

- Browser
- Postman
- Thunder Client

---

# 📁 Important Files

| File | Purpose |
|------|---------|
| manage.py | Django management utility |
| requirements.txt | Project dependencies |
| db.sqlite3 | SQLite database |
| models.py | Database models |
| serializers.py | Converts model objects into JSON |
| views.py | API request handling |
| urls.py | URL configuration |
| settings.py | Django project configuration |

---

# 📖 Learning Outcomes

Through this hands-on, I learned:

- Creating REST APIs with Django REST Framework
- Using Django models with serializers
- Handling HTTP requests and responses
- Working with JSON data
- Performing database migrations
- Managing application configuration
- Connecting backend APIs with database models

---

# 🔮 Future Enhancements

- CRUD API Operations
- Authentication & Authorization
- API Validation
- Pagination
- Filtering & Searching
- Token-based Authentication
- Swagger/OpenAPI Documentation

---

# ✅ Conclusion

This hands-on provided practical experience in developing REST APIs using Django REST Framework. It covered the complete workflow from configuring a Django project to exposing API endpoints using serializers and views. The project establishes a strong foundation for building scalable backend web services.
