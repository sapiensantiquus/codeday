import os
from config import db
from models.customer import Customer
from models.employee import Employee
from models.employee_task import EmployeeTask
from models.key import Key
from models.project import Project
from models.task import Task
from services import auth_service

def run_all():
    # Data to initialize database with

    CUSTOMERS = [
        {'name': 'K&G Creative'},
    ]
    PROJECTS = [
        {'customer_id': 1, 'title': 'New Project'},
    ]
    EMPLOYEES = [
        {'firstname': 'Andrew', 'lastname': 'Johnson', 'username': 'ajohnson', 'password': 'ajohnson'},
    ]
    TASKS = [
        {'project_id': 1, 'description': 'Just a simple task'},
    ]
    EMPLOYEE_TASKS = [
        {'employee_id': 1, 'task_id': 1, 'starttime': None, 'endtime': None},
    ]    # Create the database
    db.create_all()


    # Iterate over the book structure and populate the database
    k=b'ZyTEsBGJsLR6a_7uuB5U4y5HyagsOePeQwBz_8UJ4ZU='
    key = Key(key=k)
    db.session.add(key)

    for cust in CUSTOMERS:
        c = Customer(name=cust['name'])
        db.session.add(c)

    for proj in PROJECTS:
        p = Project(customer_id=proj['customer_id'],title=proj['title'])
        db.session.add(p)

    for emp in EMPLOYEES:
        e = Employee(firstname=emp['firstname'],lastname=emp['lastname'],username=emp['username'],password=auth_service.encrypt(k,emp['password']))
        db.session.add(e)

    for task in TASKS:
        t = Task(project_id=task['project_id'],description=task['description'])
        db.session.add(t)

    for emp in EMPLOYEE_TASKS:
        e = EmployeeTask(employee_id=emp['employee_id'],task_id=emp['task_id'])
        db.session.add(e)
    db.session.commit()

#import populate_database
#populate_database.run_all()
