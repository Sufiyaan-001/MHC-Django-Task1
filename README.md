# E-commerce Database System

## Overview

The E-commerce Database System is a web application for managing products, including clothes, electronics, and groceries. Built with Django, the system provides functionalities for adding, editing, and deleting products, with an intuitive interface for searching and filtering.

## Features

Add, update, and delete products in various categories.

Search bar for finding specific products.

Responsive design using Bootstrap.

Organized data display with filtering and sorting.

Easy navigation across product categories.

## Technologies Used

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: PostgreSQL

# Setup Instructions

## Prerequisites

Python 3.x

Django 4.x

PostgreSQL

Pipenv or virtualenv (optional but recommended)

## Installation

Clone the repository:
```cmd
git clone https://github.com/Sufiyaan-001/MHC-Django-Task1
cd MHC-Django-Task1
```
Create a virtual environment and activate it:
``` cmd
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
## Install dependencies:

pip install -r requirements.txt

Configure the database settings in settings.py:
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## Apply migrations:
Run the following Commands in the cmd.
```cmd
python manage.py makemigrations
python manage.py migrate
```
## Run the development server:
```cmd
python manage.py runserver
```
Access the application in your browser at http://127.0.0.1:8000.

## Usage

Navigate to the desired product category (e.g., clothes, electronics, groceries).

Use the "Add New Product" button to create a new record.

Search for products using the search bar.

Edit or delete records using the respective buttons in the actions column.

# Notes

Ensure the database user has the necessary permissions.

Customize the UI by modifying the Bootstrap classes in the templates.
