from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# Comments related to different kind of requests

# GET: get or return an information
# POST: create something new
# PUT: update
# DELETE: delete something


students = {
    1: {
        "name": "Rohan",
        "age": 18,
        "year": "10"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# home route
@app.get("/")
def index():
    return {"name": "Pulkit"}

# path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of student that you want to view", gt=0, lt=4)):
    return students[student_id]


# query parameter
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students [student_id]
    return {"Data": "Not Found"}

# gt --> greater than


# post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    
    students[student_id] = student
    return students[student_id]


# put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student Id does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year


    return students[student_id]


# delete method and path parameter
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student Id does not exist"}
    
    del students[student_id]
    return {"Message": "Student Id deleted successfully"}