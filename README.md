# Library Management System

This project implements a Library Management System backend using [Django](https://www.djangoproject.com/), a popular web framework for Python.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Database Schema](#database-schema)
- [API Documentation](#api-documentation)
- [Testing and Validation](#testing-and-validation)
- [Code Quality and Error Handling](#code-quality-and-error-handling)
- [Authentication Implementation (Bonus)](#authentication-implementation-bonus)

## Project Overview
The Library Management System includes models representing books and library users, demonstrating 1-1, 1-M, and M-M relationships. It provides APIs to interact with these models.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
Install dependencies:


Copy code
pip install -r requirements.txt
Run database migrations:


Copy code
python manage.py migrate
Start the development server:


Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000/api/

Database Schema
The database schema includes the following models:

User Model
Book Model
BookDetails Model
BorrowedBooks Model
API Documentation
User APIs
Create a New User:

Endpoint: /api/users/create/
Method: POST
Parameters: Name, Email, MembershipDate
List All Users:

Endpoint: /api/users/
Method: GET
Get User by ID:

Endpoint: /api/users/{user_id}/
Method: GET
Book APIs
Add a New Book:

Endpoint: /api/books/create/
Method: POST
Parameters: Title, ISBN, PublishedDate, Genre
List All Books:

Endpoint: /api/books/
Method: GET
Get Book by ID:

Endpoint: /api/books/{book_id}/
Method: GET
Assign/Update Book Details:

Endpoint: /api/books/{book_id}/update-details/
Method: PUT
Parameters: NumberOfPages, Publisher, Language
BorrowedBooks APIs
Borrow a Book:

Endpoint: /api/borrow/
Method: POST
Parameters: UserID, BookID, BorrowDate
Return a Book:

Endpoint: /api/return/
Method: PUT
Parameters: UserID, BookID, ReturnDate
List All Borrowed Books:

Endpoint: /api/borrowed-books/
Method: GET
Testing and Validation
Test each API for functionality and reliability. Ensure all CRUD operations work as intended for each model.
