# Little Lemon Restaurant - Back-End Developer Capstone

**Author:** Geoffrey Edmund Moraes

**GitHub:** https://github.com/eddietorial/gem-be-dev-capstone

**Course:** Meta Back-End Developer Capstone (Coursera)

---

## About this project

This is the capstone project for the Meta Back-End Developer Professional Certificate on Coursera. It is a Django web application for the Little Lemon restaurant with a MySQL database, a REST API for menu items and table bookings, token-based authentication, and a set of unit tests.

---

## Tech stack

- Python 3.11
- Django 5.2.12
- Django REST Framework 3.17.1
- MySQL 8
- Djoser 2.3.3 (token auth)
- Insomnia (API testing)

---

## API endpoints to test

| Method | URL | Auth required | Description |
|--------|-----|---------------|-------------|
| GET | `/restaurant/` | No | Home page |
| GET | `/restaurant/menu/` | No | Menu page (HTML) |
| GET | `/restaurant/book/` | No | Booking page (HTML) |
| GET | `/restaurant/menu/items/` | No | List all menu items |
| POST | `/restaurant/menu/items/` | No | Create a menu item |
| GET | `/restaurant/menu/items/<id>/` | No | Get a single menu item |
| PUT / PATCH | `/restaurant/menu/items/<id>/` | No | Update a menu item |
| DELETE | `/restaurant/menu/items/<id>/` | No | Delete a menu item |
| GET | `/restaurant/booking/tables/` | Yes | List all bookings |
| POST | `/restaurant/booking/tables/` | Yes | Create a booking |
| GET | `/restaurant/booking/tables/<id>/` | Yes | Get a single booking |
| PUT / PATCH | `/restaurant/booking/tables/<id>/` | Yes | Update a booking |
| DELETE | `/restaurant/booking/tables/<id>/` | Yes | Delete a booking |
| POST | `/auth/users/` | No | Register a new user |
| POST | `/auth/token/login/` | No | Obtain auth token |
| POST | `/auth/token/logout/` | Yes | Invalidate auth token |

---

## Prerequisites

- Python 3.11
- MySQL Server 8.x
- pip
- git

Install MySQL on Ubuntu/Debian:

```bash
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

---

## Setup and run

### 1. Clone the repository

```bash
git clone https://github.com/eddietorial/gem-be-dev-capstone.git
cd gem-be-dev-capstone
```

### 2. Create and activate a virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `mysqlclient` fails, first install the system libraries:

```bash
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install mysqlclient
```

### 4. Create the MySQL database and user

```bash
sudo mysql -u root -p
```

Inside the MySQL shell:

```sql
CREATE DATABASE LittleLemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON LittleLemon.* TO 'admindjango'@'localhost';
GRANT ALL PRIVILEGES ON test_LittleLemon.* TO 'admindjango'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (for the admin panel)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/restaurant/ to confirm the app is running.

---

## Running the unit tests

```bash
python manage.py test tests
```

All tests should pass with no errors.

---

## Testing the API with Insomnia

### Register a user

- Method: POST
- URL: `http://127.0.0.1:8000/auth/users/`
- Body (JSON):

```json
{
  "username": "testuser",
  "password": "TestPass123!"
}
```

### Obtain a token

- Method: POST
- URL: `http://127.0.0.1:8000/auth/token/login/`
- Body (JSON):

```json
{
  "username": "testuser",
  "password": "TestPass123!"
}
```

Copy the `auth_token` value from the response.

### Use the token

Add this header to all booking requests:

```
Authorization: Token <your_token_here>
```

### Create a booking

- Method: POST
- URL: `http://127.0.0.1:8000/restaurant/booking/tables/`
- Header: `Authorization: Token <your_token>`
- Body (JSON):

```json
{
  "name": "Geoffrey Moraes",
  "no_of_guests": 4,
  "booking_date": "2026-04-01"
}
```

### Create a menu item

No token required.

- Method: POST
- URL: `http://127.0.0.1:8000/restaurant/menu/items/`
- Body (JSON):

```json
{
  "title": "Grilled Sea Bass",
  "price": "18.50",
  "inventory": 12
}
```

---

## Project structure

```
gem-be-dev-capstone/
    manage.py
    requirements.txt
    .gitignore
    README.md
    littlelemon/
        settings.py
        urls.py
        wsgi.py
        asgi.py
    restaurant/
        admin.py
        models.py
        serializers.py
        views.py
        urls.py
        static/
            restaurant/
                littlelemon.png
    templates/
        index.html
        menu.html
        booking.html
    tests/
        test_models.py
        test_views.py
```
