# Simple CRUD Application with FastAPI, Python, and MySQL

This is a simple CRUD (Create, Read, Update, Delete) application using FastAPI (Python), HTML/JavaScript, and MySQL.

## Setup

### 1. Install Python
Download and install Python from https://python.org (version 3.7+).

### 2. Install MySQL
- Download and install MySQL Server from https://dev.mysql.com/downloads/mysql/
- During installation, set up a root password (leave blank for no password, as in the code).
- Create a database named `crud_db`:
  - Open MySQL Command Line Client or MySQL Workbench.
  - Run: `CREATE DATABASE crud_db;`

### 3. Install Dependencies
In the project folder, run:
```
pip install -r requirements.txt
```

### 4. Run the Application
Start the FastAPI server:
```
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

Open `index.html` in your browser to use the application.

## Files

- `requirements.txt`: Python dependencies
- `database.py`: Database connection setup
- `models.py`: SQLAlchemy models
- `crud.py`: CRUD operations
- `main.py`: FastAPI application
- `index.html`: Frontend HTML with JavaScript

## API Endpoints

- `GET /users`: Get all users
- `GET /users/{id}`: Get a specific user
- `POST /users`: Create a new user
- `PUT /users/{id}`: Update a user
- `DELETE /users/{id}`: Delete a user

## Note

This is a basic implementation. In production, add proper validation, authentication, and error handling.