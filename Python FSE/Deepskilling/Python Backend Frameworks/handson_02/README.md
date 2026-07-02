# Hands-On 02 – Django Models, ORM & Admin Interface

## 📖 Overview

This hands-on extends the Django Course Management project by introducing database models, Django ORM operations, migrations, and the built-in Django Administration panel.

The objective of this exercise is to design a relational database for the Course Management System, perform CRUD operations using Django ORM, and manage records through the Django Admin Interface.

---

# 🎯 Objectives

- Design database models using Django ORM.
- Understand model relationships.
- Perform database migrations.
- Execute CRUD operations using Django Shell.
- Register models in Django Admin.
- Customize the Admin Interface.
- Verify model constraints.

---

# 🛠 Technologies Used

- Python 3
- Django
- SQLite Database
- Django ORM
- Django Admin
- VS Code

---

# 📂 Project Structure

```
handson_02/
│
├── coursemanager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── courses/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── migrations/
│   └── ...
│
├── db.sqlite3
├── manage.py
├── output of task2.png
└── README.md
```

---

# 📚 Concepts Covered

## Django Models

Models define the structure of the database tables using Python classes.

Implemented entities include:

- Department
- Course
- Student
- Enrollment

Each model contains attributes that are mapped directly to database columns.

---

## Database Migrations

Database changes are managed using migrations.

Commands used:

```bash
python manage.py makemigrations
python manage.py migrate
```

These commands automatically generate and apply database schema changes.

---

## Django ORM

The Django Object Relational Mapper (ORM) allows database operations without writing SQL queries directly.

Operations performed include:

- Create
- Retrieve
- Update
- Delete
- Filter
- Aggregate Queries

---

## Django Admin

The Django Admin site provides an easy interface to manage application data.

Registered models can be viewed, edited, searched, and deleted without creating additional user interfaces.

---

# ⚙ Features Implemented

- Department Model
- Course Model
- Student Model
- Enrollment Model
- Foreign Key Relationships
- Model Registration
- Admin Dashboard
- ORM Queries
- CRUD Operations
- Database Migrations

---

# 🚀 Installation

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

Create administrator account.

```bash
python manage.py createsuperuser
```

Run the project.

```bash
python manage.py runserver
```

---

# 📸 Output

The project includes screenshots demonstrating the successful execution of the tasks.

```
output of task2.png
```

---

# 📁 Important Files

| File | Description |
|------|-------------|
| manage.py | Django management utility |
| db.sqlite3 | SQLite database |
| models.py | Database models |
| admin.py | Admin configuration |
| settings.py | Project settings |
| urls.py | URL configuration |

---

# 📖 Learning Outcomes

Through this hands-on, I learned:

- Creating Django models
- Performing migrations
- Understanding database relationships
- Using Django ORM effectively
- Managing data through Django Admin
- Working with SQLite databases
- Performing CRUD operations

---

# 📌 Future Enhancements

- REST API Integration
- Authentication
- Serializer Implementation
- ViewSets
- Pagination
- Search Functionality

---

# ✅ Conclusion

This hands-on provided practical experience in designing relational database models using Django. It strengthened my understanding of ORM concepts, database migrations, model relationships, and the Django Admin Interface. These concepts form the foundation for building scalable backend applications using Django.
