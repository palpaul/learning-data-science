# import fast api
# fast api is hte predefined library for building APIs in python

from fastapi import FastAPI


# import BaseModel
#BaseModel used to define schema for the data that we want to send and receive from the API     
from pydantic import BaseModel
# crate the object of the fast api(instance of the fast api)
app = FastAPI()
# define the schema for the data that we want to send and receive from the API  
# define the schema (rulesand Regulations) for the data that we want to send and receive from the API   
class Employee(BaseModel):
    emp_id: int
    emp_name: str
    department: str
    salary: float
    experience: int
    email: str
    is_active: bool

# dummay data for testing the API
employees = [{
    "emp_id": 1,
    "emp_name": "John Doe",
    "department": "IT",
    "salary": 50000.0,
    "experience": 5,
    "email": "john.doe@example.com",
    "is_active": True
},
{
    "emp_id": 2,
    "emp_name": "Jane Smith",
    "department": "HR",
    "salary": 55000.0,
    "experience": 3,
    "email": "jane.smith@example.com",
    "is_active": True
},]

# how to create a get method to fetch the employee data from the list

@app.get("/")
def read_root():
    return {"message": "Welcome to the fast API"}

@app.get("/get_employees")
def get_employees():
    return employees

# how do i run this API
# to run this API we need to use the command uvicorn main:app --reload
# uvicorn is the server that we use to run the API
# main is the name of the file where we have defined the API
# app is the name of the object that we have created for the fast API
# --reload is used to reload the server automatically when we make changes to the code


# how can i see the swagger documentation for this API
# to see the swagger documentation for this API we need to go to the url http://localhost:8000/docs
# this will open the swagger documentation for this API where we can see all the endpoints and test
# redoc 
# to see the redoc documentation for this API we need to go to the url http://localhost:8000/redoc
# this will open the redoc documentation for this API where we can see all the endpoints and
# test the API

@app.get("/get_employee/{emp_id}")
def get_employee(emp_id: int):
    for employee in employees:
        if employee["emp_id"] == emp_id:
            return employee
    return {"message": "Employee not found"}

@app.get("/employees")
def get_all_employees():
    return {
        "total_employees": len(employees),
        "data": employees
    }