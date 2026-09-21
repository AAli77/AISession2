from pydantic import BaseModel

#API request validation using Pydantic

class Student(BaseModel):
    name: str
    age: int
    course: str

student= Student(
    name="Amir Ali", 
    age=56, 
    course="Computer Science")

print(student.name)  # Output: John Doe
