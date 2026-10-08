# Student Management API

A simple CRUD-based Student Management REST API built using FastAPI and Pydantic.

## Features

- Create a student
- Get all students
- Get a student by ID
- Update a student
- Delete a student
- Pydantic data validation
- Proper HTTP status codes
- Interactive Swagger UI documentation

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
student_management_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all API endpoints.

## API Endpoints

| Method | Endpoint | Description | Status Code |
|---|---|---|---|
| GET | `/` | Check API status | 200 |
| POST | `/students` | Create student | 201 |
| GET | `/students` | Get all students | 200 |
| GET | `/students/{student_id}` | Get student by ID | 200 |
| PUT | `/students/{student_id}` | Update student | 200 |
| DELETE | `/students/{student_id}` | Delete student | 204 |

## Student Fields

A student contains:

```json
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 25,
    "course": "Python"
}
```

For POST and PUT requests, `id` is generated/managed by the API.

## POST /students

Create a new student.

Example request:

```json
{
    "name": "Sanjeet",
    "email": "sanjeet@gmail.com",
    "age": 40,
    "course": "FastAPI"
}
```

Successful response:

```json
{
    "id": 3,
    "name": "Sanjeet",
    "email": "sanjeet@gmail.com",
    "age": 40,
    "course": "FastAPI"
}
```

Status code:

```text
201 Created
```

## GET /students

Returns all students.

Example response:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "age": 25,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "email": "priya@gmail.com",
        "age": 23,
        "course": "FastAPI"
    }
]
```

Status code:

```text
200 OK
```

## GET /students/{student_id}

Example:

```text
GET /students/1
```

Response:

```json
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 25,
    "course": "Python"
}
```

If the student does not exist:

```json
{
    "detail": "Student not found"
}
```

Status code:

```text
404 Not Found
```

## PUT /students/{student_id}

Example:

```text
PUT /students/1
```

Request:

```json
{
    "name": "Rahul Kumar",
    "email": "rahulkumar@gmail.com",
    "age": 26,
    "course": "Data Science"
}
```

Status code:

```text
200 OK
```

## DELETE /students/{student_id}

Example:

```text
DELETE /students/1
```

If the student exists, the student is actually removed from the in-memory data.

Status code:

```text
204 No Content
```

If the student does not exist:

```text
404 Not Found
```

## Pydantic Validation

The API validates:

- Name length
- Email format
- Age range
- Course length

Example invalid email:

```json
{
    "name": "Test",
    "email": "invalid-email",
    "age": 25,
    "course": "Python"
}
```

FastAPI returns a validation error with status code:

```text
422 Unprocessable Entity
```

## Important Note

This project uses an in-memory Python dictionary instead of a database.

Therefore, data will be reset whenever the FastAPI application is restarted.

## Testing

All APIs can be tested using:

- Swagger UI
- Postman

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## GitHub

The complete source code will be pushed to GitHub.

## YouTube Demonstration

The YouTube video will demonstrate:

1. Project structure
2. Code explanation
3. POST API
4. GET all students
5. GET student by ID
6. PUT student
7. DELETE student
8. Validation error
9. 404 error
10. Swagger UI testing

## Author

Sanjeet Kumar