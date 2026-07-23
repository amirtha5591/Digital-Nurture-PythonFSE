# Hands-On 05 – Flask SQLAlchemy Database Integration and Flask-Migrate

## 📖 Overview

This hands-on focuses on integrating a relational database with a Flask application using SQLAlchemy ORM. It also demonstrates database version control using Flask-Migrate, enabling efficient schema management through migrations.

The project follows a modular Flask architecture by separating application configuration, database models, routes, and migration files for better maintainability and scalability.

---

# 🎯 Objectives

- Develop backend applications using Flask.
- Configure SQLAlchemy with Flask.
- Create relational database models.
- Perform database migrations using Flask-Migrate.
- Organize backend code into reusable modules.
- Build REST-ready backend architecture.

---

# 🛠 Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask-Migrate
- SQLite
- VS Code

---

# 📂 Project Structure

```
handson_05/
│
├── courses/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│
├── migrations/
│   ├── versions/
│   └── ...
│
├── instance/
│   └── course.db
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# 🚀 Features Implemented

- Flask Application Setup
- SQLAlchemy ORM Integration
- SQLite Database Configuration
- Flask-Migrate Support
- Modular Project Architecture
- Database Models
- API Route Configuration
- Database Migration Management

---

# 📚 Key Concepts Covered

## Flask Framework

Flask is a lightweight Python framework used to develop web applications and REST APIs with minimal configuration.

---

## SQLAlchemy ORM

SQLAlchemy allows database operations using Python objects instead of writing raw SQL queries.

Implemented features include:

- Database connection
- Model creation
- Table mapping
- CRUD-ready architecture

---

## Flask-Migrate

Flask-Migrate manages database schema changes through migration scripts.

Common commands:

```bash
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
```

---

## SQLite Database

SQLite is used as the backend relational database during development.

The database is stored inside the **instance** directory.

---

## Modular Design

The application separates responsibilities into different modules.

- Configuration
- Database Models
- Routes
- Migrations
- Application Entry Point

This improves code readability and maintainability.

---

# ⚙ Installation

Clone the repository.

Install dependencies.

```bash
pip install -r requirements.txt
```

Run database migrations.

```bash
flask db upgrade
```

Start the Flask server.

```bash
python app.py
```

---

# 📁 Important Files

| File | Description |
|------|-------------|
| app.py | Flask application entry point |
| config.py | Project configuration |
| models.py | Database models |
| routes.py | API endpoints |
| migrations/ | Database migration history |
| instance/ | SQLite database storage |
| requirements.txt | Project dependencies |

---

# 📖 Learning Outcomes

After completing this hands-on, I learned:

- Flask application development
- SQLAlchemy ORM integration
- Database migrations using Flask-Migrate
- SQLite database management
- Organizing backend applications
- Building scalable Flask projects
- Managing application configuration

---

# 🔮 Future Enhancements

- Complete CRUD Operations
- RESTful API Development
- User Authentication
- Request Validation
- Error Handling
- JWT Authentication
- Swagger API Documentation

---

# ✅ Conclusion

This hands-on provided practical experience in integrating SQLAlchemy with Flask and managing database schema changes using Flask-Migrate. It strengthened my understanding of ORM concepts, database version control, and modular backend development practices. These concepts form the foundation for developing scalable Flask-based REST APIs.
