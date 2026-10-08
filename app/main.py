from fastapi import FastAPI,HTTPException,status 
from app.models import students 
from app.schemas import StudentCreate,StudentUpdate,StudentResponse 

app = FastAPI(
    title = 'Student Management API',
    description = 'CRUD API for managing students',
    version = '1.0.0'
)

@app.get('/')
def home():
    return {'message':'Student Management API is running'}

@app.post( 
    '/students',
    response_model = StudentResponse,
    status_code = status.HTTP_201_CREATED 

)
def create_student(student:StudentCreate):
    new_id = max(students.keys(),default = 0) + 1 
    new_student = { 
        'id': new_id,
        'name': student.name,
        'email':student.email,
        'age': student.age,
        'course':student.course 
    }

    students[new_id] = new_student 
    return new_student 

# GET ALL STUDENTS 

@app.get(
    '/students',
    response_model = list[StudentResponse],
    status_code = status.HTTP_200_OK

)
def get_students():
    return list(students.values())

# GET STUDENT BY ID 

@app.get( 
    '/students/{student_id}',
    response_model = StudentResponse,
    status_code = status.HTTP_200_OK 

)
def get_student(student_id:int):
    if student_id not in students:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Student not found'

        )
    return students[student_id] 

# UPDATE STUDENT 

@app.put(

'/students/{student_id}',
response_model = StudentResponse,
status_code = status.HTTP_200_OK
)
def update_student(student_id:int,student:StudentUpdate):
    if student_id not in students:
        raise HTTPException( 
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Student not found' 

        )
    updated_student = {'id':student_id,'name':student.name,'email':student.email,'age':student.age,'course':student.course}
    students[student_id] = updated_student 
    return updated_student 

# DELETE STUDENT 

@app.delete('/students/{student_id}',status_code = status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException( 
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Student not found'

        )
    del students[student_id]
    return None 

