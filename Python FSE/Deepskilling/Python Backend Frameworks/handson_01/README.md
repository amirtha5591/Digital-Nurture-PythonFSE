# Hands-On 01 – Django Project Setup & Web Framework Fundamentals

## Overview

This hands-on introduces the fundamentals of backend web development using the Django framework. The primary goal is to understand how a Django application is structured and how HTTP requests are processed from the client to the server. It also covers the creation of a Django project, application configuration, URL routing, and a simple response using a function-based view.

By completing this exercise, I became familiar with Django's project architecture and the basic workflow involved in developing backend applications.

---

## Objectives

- Understand the purpose of a web framework.
- Learn the HTTP Request–Response lifecycle.
- Understand the MVC and Django MVT architecture.
- Create a Django project and application.
- Configure project settings.
- Register applications in Django.
- Implement URL routing.
- Create and test a basic HTTP response.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Django | Backend Web Framework |
| VS Code | Development Environment |
| SQLite | Default Django Database |

---

## Project Structure

```
handson_01/
│
├── coursemanager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── ...
│
├── courses/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Key Concepts Covered

### Django Project

A Django project acts as the main configuration container for the entire application. It contains global settings, URL configurations, and deployment files.

### Django App

An application is a reusable module responsible for implementing a specific functionality within the project. Multiple apps can exist inside a single Django project.

### Request–Response Cycle

The request follows the sequence below:

```
Browser
      │
      ▼
URL Configuration
      │
      ▼
View Function
      │
      ▼
Business Logic
      │
      ▼
HTTP Response
      │
      ▼
Browser
```

### MVC vs MVT

| MVC | Django MVT |
|------|------------|
| Model | Model |
| View | Template |
| Controller | View |

Django follows the MVT (Model–View–Template) architecture, where the framework itself manages most controller responsibilities.

---

## Features Implemented

- Django project creation
- Application creation
- Application registration
- URL configuration
- Function-based view
- HTTP response generation
- Development server execution

---

## Installation

Clone the repository.

Install the required packages.

```bash
pip install -r requirements.txt
```

Run database migrations.

```bash
python manage.py migrate
```

Start the development server.

```bash
python manage.py runserver
```

Open the browser and visit:

```
http://127.0.0.1:8000/api/hello/
```

---

## Expected Output

The application successfully returns the following response:

```
Course Management API is running
```

---

## Learning Outcomes

After completing this hands-on, I gained practical knowledge about:

- Django project architecture
- Creating Django applications
- URL routing mechanism
- Function-based views
- HTTP request and response flow
- Project configuration using `settings.py`
- Running and testing Django applications

---

## Challenges Faced

During development, I explored Django's folder structure and learned how different configuration files work together. Understanding URL routing and application registration helped me gain confidence in organizing backend projects effectively.

---

## Future Improvements

The next steps for this project include:

- Creating database models
- Performing CRUD operations
- Using Django ORM
- Building REST APIs
- Integrating Django REST Framework

---

## Conclusion

This hands-on served as the foundation for learning backend development with Django. It introduced the essential concepts required to build scalable web applications and prepared the environment for implementing database operations, REST APIs, and advanced backend features in subsequent exercises.
