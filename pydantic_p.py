from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str

student= Student(
    name="John Doe", 
    age=20, 
    course="Computer Science")

print(student.name)  # Output: John Doe
