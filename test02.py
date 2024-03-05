from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    id:int
    name:str
    surname:str
    age:int

students_list = [
    Students(id=1, name="Raul", surname="Papir",age=10),
    Students(id=2, name="Pepa", surname="Pig",age=400),
    Students(id=3, name="Flor", surname="Peña", age=56),
    Students(id=4, name="Kvote", surname="kon", age=26)
]

@app.get("/students/")
async def students():
    return students_list

@app.get("/student/{id}")
async def student(id:int):
    return get_student(id)

@app.post("/add_student/",response_model=Students)
async def add_new_studenr(user:Students):
    return create_student(user)

# Create a Student.
def create_student(user:str):
    student_found=filter(lambda user: user.id == id, students_list)
    if list(student_found)[0] == students_list[0]:
        raise HTTPException(status_code=200,detail="The student is already in the list.")

    else:
        students_list.append(user)


# Iterate a Student list.
def get_student(id:int):
    student_found=filter(lambda Students: Students. id == id, students_list)
    try:
        return list(student_found)[0]
    except:
        raise HTTPException(status_code=404, detail="Student Id not found")