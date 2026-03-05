# Simple CRUD Application

A simple CRUD (Create, Read, Update, Delete) application using FastAPI, Python, and MySQL.

## Quick Start

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Setup MySQL:**
   - Create database: `CREATE DATABASE crud_db;`
   - Intilize the Sql Url in `database.py`
3. **Run the server:**
   ```
   uvicorn main:app --reload
   ```

4. **Open in browser:**
   - Open `index.html` to use the application

## Features

- Create, Read, Update, and Delete users
- Simple HTML/JavaScript frontend
- FastAPI backend with MySQL database

## Files

- `main.py` - FastAPI application
- `index.html` - Frontend interface
- `database.py` - Database configuration
- `models.py` - Database models
- `crud.py` - CRUD operations