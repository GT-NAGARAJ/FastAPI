from fastapi import FastAPI, HTTPException
from model_validation import Employee
from typing import List

app=FastAPI()

employee_db: List[Employee] = []

#1. Read all employees 
@app.get('/employees', response_model=List[Employee])
def get_employees():
    return employee_db

#2. Get a specific Employee  ( Path Parameter )
@app.get('/employees/{EmpId}', response_model=Employee)
def get_employee(EmpId: int):
    for employee in employee_db:
        if employee.id == EmpId:
            return employee
    raise HTTPException(status_code=400, detail='Employee Not found')

#3. Add a employee ( POST )
@app.post('/add_employee',response_model=Employee)
def add_employee(new_Emp: Employee):
    for index, employee in enumerate(employee_db):
        if employee.id == new_Emp.id:
            raise HTTPException(status_code=404, detail='Employee Already existed') 
    employee_db.append(new_Emp)
    return new_Emp

#4. Updated Employee Dep ( PUT )
@app.put('/update_employee/{employee_id}', response_model=Employee)
def update_employee(employee_id: int, update_employee: Employee):
    for index, employee in enumerate(employee_db):
        if employee.id == employee_id:
            employee_db[index]=update_employee
            return update_employee
    raise HTTPException(status_code=404, detail='Employee Not Found')
            

#5. Delete the employee (Delete)
@app.delete('/delete_employee/{employee_id}')
def delete_employee(employee_id: int):
    for index, employee in enumerate(employee_db):
        if employee.id == employee_id:
            employee_db.remove(employee)
            return {'message': 'Employee with {employee_id} is deleted successfully'}
    raise HTTPException(status_code=400, detail='Employye with that ID is not Found')

#

