# Hands-On 04 – Flask Application with SQLAlchemy Database Integration

## 📖 Overview

This hands-on introduces backend development using the Flask framework. The project demonstrates how to configure a Flask application, organize project files, integrate SQLAlchemy for database management, and structure a modular backend application.

The application follows a simple and maintainable architecture by separating configuration, application logic, and database models into different modules.

---

# 🎯 Objectives

- Understand the Flask framework.
- Configure a Flask application.
- Learn Flask project structure.
- Integrate SQLAlchemy ORM.
- Organize routes and models using modular design.
- Build a backend application with database connectivity.

---

# 🛠 Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- SQLite
- VS Code

---

# 📂 Project Structure

```
handson_04/
│
├── courses/
│   ├── models.py
│   ├── routes.py
│   ├── __init__.py
│
├── app.py
├── config.py
├── README.md
```

---

# 🚀 Features Implemented

- Flask Application Setup
- SQLAlchemy Database Configuration
- Modular Project Structure
- Configuration Management
- Route Management
- ORM Integration
- SQLite Database Connectivity

---

# 📚 Key Concepts Covered

## Flask Framework

Flask is a lightweight Python web framework used for developing web applications and REST APIs.

---

## SQLAlchemy ORM

SQLAlchemy is used as the Object Relational Mapper (ORM) to interact with the SQLite database using Python classes instead of SQL queries.

---

## Configuration Management

Application settings such as database URI and debugging options are managed separately in `config.py`, improving maintainability.

---

## Modular Architecture

The project separates different functionalities into dedicated modules.

- Application Entry Point
- Configuration
- Models
- Routes

This makes the application easier to extend and maintain.

---

# ⚙ Installation

Clone the repository.

Install required packages.

```bash
pip install -r requirements.txt
```

Run the Flask application.

```bash
python app.py
```

The application will start on the default Flask development server.

---

# 📁 Important Files

| File | Description |
|------|-------------|
| app.py | Main Flask application |
| config.py | Application configuration |
| models.py | Database models |
| routes.py | API routes |
| __init__.py | Package initialization |

---

# 📖 Learning Outcomes

After completing this hands-on, I learned:

- Flask application development
- Project organization
- SQLAlchemy integration
- Database configuration
- Route handling
- Modular backend architecture
- SQLite database connectivity

---

# 🔮 Future Enhancements

- CRUD Operations
- REST API Development
- User Authentication
- Input Validation
- Error Handling
- API Documentation
- Deployment on Cloud Platforms

---

# ✅ Conclusion

This hands-on provided practical experience in building backend applications using Flask. It demonstrated how to organize a Flask project, configure SQLAlchemy, and structure application components efficiently. The concepts learned here serve as a foundation for developing scalable RESTful backend services.
