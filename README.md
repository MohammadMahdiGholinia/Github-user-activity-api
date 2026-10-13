# GitHub User Activity API

A REST API built with **Django** and **Django REST Framework** that retrieves a GitHub user's public events and returns them in a simplified format.

The project also uses Redis-compatible caching through Memurai to reduce repeated requests to the GitHub API.

---

## Features
- Retrieve public events for a GitHub user
- Simplify GitHub event types
- Handle GitHub API errors
- Cache responses for 5 minutes using Redis

---

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/MohammadMahdiGholinia/Github-user-activity-api.git
```

### 2. Create a virtual environment
```bash
python -m venv venv
```
Activate the virtual environment.

**Windows PowerShell:**

```bash
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start Redis
Start your local Redis-compatible server, such as Memurai, and make sure it is listening on `127.0.0.1:6379.`

The Django cache configuration currently uses Redis database1.

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Start the development server
```bash
python manage.py runserver
```

### 7. Try the API

Open the following URL in your browser:
```bash
http://127.0.0.1:8000/api/github/events/?username=<username>
```


## Development

This project is currently intended for learning and development purposes.