
from fastapi import FastAPI, Path, HTTPException
import uvicorn
from typing import Optional
from pydantic import BaseModel

# MOST IMP. THING
app = FastAPI() 


Students={
    1:{
        'name':'Mariam',
        "age":20,
        "color":"purple"
    },

    2:{
        "name":'Ali',
        'age':18,
        'color':'blue'
    }
}

#----------------------------
class Student(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    date_year: Optional[int]=None

#--------------------------
@app.get("/")
def home():
    return {"message": "Hello fastAPI"}


@app.get("/Students/{stu_id}")
def get_student(stu_id: int = Path(..., description="Enter the student ID", gt=0, lt=3)):
    student = Students.get(stu_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
# gt= greater than
#  lt= lower than
# ge = greater than or equal to
if __name__ == "__main__":
    uvicorn.run("myapp:app", host="127.0.0.1", port=8000, reload=True)


#------------- Query parameters --------------------
# ex: google.com/results?search=python
# "search=python" --> query parameters (key=vlaue) 
#  on the same end point we can have multiple query parameters
# None == not required
# optional == not required and can be None
# optional argumants are last!

@app.get("/get-by-name") # unlike path parameters, query parameters are optional

# no error , optional parameter is last
# * = keyword only argument
def get_stu_by_name(*, name: Optional[str] = None, test: Optional[int] = None):
    if not name:
        return {'Data': 'Name query parameter required'}
    for stu_id, stu in Students.items():
        if stu.get('name') == name:
            return stu
    return {'Data': 'Not found'}


# -------------------------- request body and the POST method --------------------------------
@app.post('/add-student/{stu_id}')
def add_student(stu_id: int, student: Student): # class object is passed as a parameter
    if stu_id in Students:
        raise HTTPException(status_code=400, detail="Student already exists")
    Students[stu_id] = student.dict()
    return Students[stu_id]

#--------------------------- PUT method --------------------------------------
# UPDATE existing data
@app.put("/update-student/{stu_id}")
def update_student(stu_id: int, student: Student):
    if stu_id not in Students:
        raise HTTPException(status_code=404, detail="Student does not exist")

    if student.name is not None:
        Students[stu_id]['name'] = student.name

    if student.age is not None:
        Students[stu_id]['age'] = student.age

    if student.date_year is not None:
        Students[stu_id]['date_year'] = student.date_year

    return Students[stu_id]


# --------------------------- DELETE method -----------------------
@app.delete("/delete-student/{stu_id}")

def delete_student(stu_id: int):
    if stu_id not in Students:
        return {'Error': "Student does not exist"}
    
    del Students[stu_id]
    return {'Message':'Student deleted successfully'}



@app.get('/about')
def about():
    return {'data': {"MSG":"This is about page =)"}}

#-------------------------------------------------------------------------------------------------------
# uvicorn filename (no extension): app (FastAPI instance) --reload
#--------------------------------------------------------------------------------------------------------

@app.get("/blog/{id}")
def fetch_blog_id(id :int):
    return {'DATA': id}

# FastAPI reads line by line
#Pydantic Models : Define request and response schemas with automatic validation.




