import json

# Define a function to read and load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Example usage
file_path = 'test.json'  # Replace 'example.json' with the path to your JSON file
json_data = load_json(file_path)

# Access the loaded JSON data
print(json_data["initial_songs"])
##################################

{
  "company": "TechCorp",
  "location": "New York",
  "employees": [
    {
      "id": 1,
      "name": "John Doe",
      "position": "Software Engineer",
      "department": "Engineering",
      "salary": 80000
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "position": "Data Scientist",
      "department": "Data Science",
      "salary": 90000
    },
    {
      "id": 3,
      "name": "Alice Johnson",
      "position": "Product Manager",
      "department": "Product Management",
      "salary": 100000
    }
  ]
}


#################################
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import json

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    position: str
    department: str
    salary: float

# Load initial data from JSON file
with open("employees.json", "r") as file:
    employees_data = json.load(file)

# Helper function to save data back to JSON file
def save_data(data: Dict):
    with open("employees.json", "w") as file:
        json.dump(data, file, indent=2)

@app.get("/employees/", response_model=List[Employee])
async def read_employees():
    return employees_data.get("employees", [])

@app.post("/employees/")
async def create_employee(employee: Employee):
    employees = employees_data.get("employees", [])
    employees.append(employee.dict())
    employees_data["employees"] = employees
    save_data(employees_data)
    return {"message": "Employee created successfully"}

@app.put("/employees/{employee_id}")
async def update_employee(employee_id: int, employee: Employee):
    employees = employees_data.get("employees", [])
    for emp in employees:
        if emp["id"] == employee_id:
            emp.update(employee.dict())
            break
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
    save_data(employees_data)
    return {"message": "Employee updated successfully"}

@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    employees = employees_data.get("employees", [])
    for i, emp in enumerate(employees):
        if emp["id"] == employee_id:
            del employees[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees_data["employees"] = employees
    save_data(employees_data)
    return {"message": "Employee deleted successfully"}
