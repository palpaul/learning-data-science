from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

#MongoDB connection
#MONGODB_URL = "mongodb+srv://admin:admin@palrahul.ql6of7i.mongodb.net/?appName=PalRahul"
MONGODB_URL = "mongodb+srv://admin:admin@palrahul.ql6of7i.mongodb.net/company_db?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGODB_URL)
db = client["company_db"] # db name is company_db
collection = db["employees"] # table name is employees


#Employe BaseModel
class Employee(BaseModel):
    emp_id: int
    emp_name: str
    department: str
    salary: float
    experience: int
    email: str
    is_active: bool


#home api (root api to check if the API is working or not)
@app.get("/")
async def read_root():
    return {"message": "Welcome to the fast API with mongo db"}

@app.get("/test")
async def test():
    await collection.insert_one({"test": "working"})
    return {"msg": "inserted"}

@app.get("/test2")
async def test():
    try:
        await collection.insert_one({"test": "ok"})
        return {"msg": "inserted"}
    except Exception as e:
        return {"error": str(e)}

#get employee by id (single employee data )
@app.get("/get_employee/{emp_id}")  
async def get_employee(emp_id: int):
    employee = await collection.find_one({"emp_id": emp_id})
    if employee:
        employee.pop("_id", None)  # Remove the MongoDB ObjectId
        return employee
    return {"message": "Employee not found"}



# get all employees data from the database and return the total number of employees and the data of all employees in the response
class EmployeeResponse(BaseModel):
    total_employees: int
    data: List[Employee]

@app.get("/getAllEmployees", response_model=EmployeeResponse)
async  def get_all_employees():
    data = []
    cursor = collection.find()
    async for emp in cursor:
        emp.pop("_id", None)  # Remove the MongoDB ObjectId
        data.append(emp)
    return {
        "total_employees": len(data),
        "data": data 
    }


@app.post("/add_employee")
async def add_employee(employee: Employee):
    await collection.insert_one(employee.dict())
    return {"message": "Employee added successfully", "employee": employee}

#update employee data by id
@app.put("/update_employee/{emp_id}")
async def update_employee(emp_id: int, employee: Employee):
    result = await collection.update_one(
        {"emp_id": emp_id},
        {"$set": employee.dict()} # $set is used to update the existing data with the new data provided in the employee object
    )
    if result.matched_count:
        return {
            "message": "Employee updated successfully",
            "employee": employee
        }
    return {"message": "Employee not found"}

#delete employee data by id
@app.delete("/delete_employee/{emp_id}")
async def delete_employee(emp_id: int):
    result = await collection.delete_one({"emp_id": emp_id})
    if result.deleted_count:
        return {"message": "Employee deleted successfully"}
    return {"message": "Employee not found"}