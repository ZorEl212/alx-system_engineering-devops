#!/usr/bin/python3
"""Get employee information using restful api"""
import requests
from sys import argv


def emp_status(emp_id):
    res = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    emp = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}").json()

    emp_tasks = ()
    tasks = []
    emp_name = emp['name']
    for item in res:
            if item['userId'] == int(emp_id):
                tasks.append(item)

    for task in tasks:
        if task['completed'] == True:
            emp_tasks += (task['title'],)

    print(f"Employee {emp_name} is done with tasks"
        f"({len(emp_tasks)}/{len(tasks)}):")


    for t in emp_tasks:
        print(f"\t {t}")

if __name__ == '__main__':
    if len(argv) < 2:
        print("Please input employee id")
        exit()
    emp_status(argv[1])
    
    