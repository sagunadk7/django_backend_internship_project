## 🤖 Telegram Bot Django

A Django-based backend system for managing Telegram bot users and sending emails, with JWT authentication, Celery for asynchronous tasks, and Redis as the broker.

---

## 🚀 Features

- Django REST API with public and protected endpoints
- JWT-based authentication using `rest_framework_simplejwt`
- SQLite database (default)
- Email sending via Gmail SMTP
- Background task processing with Celery and Redis
- Telegram Bot integration (`telegrambot.py`)

---

## 📦 Tech Stack

- Django 5.2.3
- Django REST Framework 3.16.0
- Simple JWT 5.5.0
- Celery 5.5.3
- Redis 6.2.0
- Python Telegram Bot ~22.1

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sagunadk7/django_backend_internship_project.git
cd django_backend_internship_project/telegrambot_project
```

### 2. Create a virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

---

## 🔐 Email & Auth Setup

Gmail SMTP (in `settings.py`):

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

JWT Settings:

```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

telegrambot.py

```python
API_KEY = 'YOUR-TELEGRAMBOT-API'
```

---

## 🧪 Running Locally

```bash
# Start Redis
redis-server

# Terminal 1: Start Django
python manage.py runserver

# Terminal 2: Start Celery worker
celery -A telegrambot_project worker --loglevel=info

# Terminal 3: Run the Telegram bot
python telegrambot.py
```

---

## 📁 Project Structure

```text
telegrambot_project/                # Python virtual environment
├── api/                      # Main API application
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── mypagination.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls_protected.py
│   ├── urls_public.py
│   └── views.py
│
├── telegrambot_project/      # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/                # HTML templates
│   ├── 404.html
│   ├── home_page.html
│   ├── login_page.html
│   └── signup_page.html
│
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   ├── user_urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
└── telegrambot.py
```

---

## ⚠️ Security Reminder

- Do not expose your `SECRET_KEY` or email credentials in a public repo.
- Set `DEBUG = False` in production.

---
# 📡 Telegram Bot User API

A RESTful Django-based API for managing Telegram bot users, with public read-only access and protected authenticated CRUD operations using JWT authentication.

---

## 🚀 API Overview

| Endpoint                  | Access     | Methods                      | Description                                 |
|---------------------------|------------|------------------------------|---------------------------------------------|
| `/public/api/items/`      | Public     | `GET`                        | List Telegram users (limited fields)        |
| `/protected/api/items/`   | Protected  | `GET, POST, PUT, PATCH, DELETE` | Full CRUD with authentication required |
| `/api/token/`             | Public     | `POST`                       | Obtain JWT access & refresh tokens          |
| `/api/token/refresh/`     | Public     | `POST`                       | Refresh JWT access token                    |

---

## 🔐 Authentication
Protected APIs use JWT Authentication.

You can get your username and password by first registering at the signup page after running the server.
Visit: http://127.0.0.1:8000/signup/ to create an account.
Protected APIs use **JWT Authentication**. You can obtain a token from:

### `POST /api/token/`

**Request:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**

```json
{
  "access": "ACCESS_TOKEN_STRING",
  "refresh": "REFRESH_TOKEN_STRING"
}
```

Use the access token in the `Authorization` header:

```http
Authorization: Bearer ACCESS_TOKEN_STRING
```

---

## 📂 API Endpoints

### 📘 `GET /public/api/items/`

- **Access**: Public  
- **Auth**: ❌ Not required  
- **Description**: Returns a paginated list of all Telegram users with limited fields.

**Response:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "telegrambot"
    }
  ]
}
```

---

### 🔐 `GET /protected/api/items/`

- **Access**: Authenticated  
- **Auth**: ✅ JWT or session required  
- **Description**: Returns a paginated list of users with full details.

**Response:**

```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "telegram_id": 123456789,
      "username": "telegrambot",
      "first_name": "telegram",
      "last_name": "user",
      "is_bot": false,
      "language_code": "en"
    }
  ]
}
```

---

### 🔐 `POST /protected/api/items/`

- **Access**: Authenticated  
- **Auth**: ✅ Required  
- **Description**: Create a new Telegram user entry.

**Request:**

```json
{
  "telegram_id": 987654321,
  "username": "newuser",
  "first_name": "New",
  "last_name": "User",
  "is_bot": false,
  "language_code": "en"
}
```

**Response:**

```json
{
  "id": 2,
  "telegram_id": 987654321,
  "username": "newuser",
  "first_name": "New",
  "last_name": "User",
  "is_bot": false,
  "language_code": "en"
}
```

---

### 🔐 `PUT /protected/api/items/<id>/`

- **Access**: Authenticated  
- **Description**: Update a Telegram user entry by ID.

---

### 🔐 `DELETE /protected/api/items/<id>/`

- **Access**: Authenticated  
- **Description**: Delete a Telegram user entry by ID.

---

## 📦 Pagination

This API uses custom pagination with the following parameters:

- `mylimit`: Number of results per page (default: `10`, max: `15`)
- `myoffset`: Number of items to skip

**Example:**

```
GET /public/api/items/?mylimit=5&myoffset=10
```

---

## 🧩 User Model

```python
class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    language_code = models.CharField(max_length=10, null=True, blank=True)
```

---

## 🧪 Example Usage (HTTPie)

```bash
http POST http://127.0.0.1:8000/api/token/ username=admin password=admin123
http GET http://127.0.0.1:8000/protected/api/items/ "Authorization: Bearer <ACCESS_TOKEN>"
```

---

## ⚠️ Error Codes

| Status Code | Meaning       |
|-------------|----------------|
| 200         | OK             |
| 201         | Created        |
| 400         | Bad Request    |
| 401         | Unauthorized   |
| 403         | Forbidden      |
| 404         | Not Found      |

---



## 📃 License

Made with ❤️ by Sagun Adhikari