#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import requests
from sys import argv

def get_user_info(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{url}users/{user_id}")
    
    user_info = user_response.json()
    return user_info

def get_completed_tasks(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    tasks_response = requests.get(f"{url}todos?userId={user_id}")
    
    tasks = tasks_response.json()
    completed_tasks = [task for task in tasks if task.get("completed")]
    values = [tasks, completed_tasks]
    return values

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = argv[1]
        user_info = get_user_info(user_id)

        name = user_info.get("name")
        
        if name is not None:
            values = get_completed_tasks(user_id)
            completed_tasks = values[0]
            all_tasks_count = len(values[1])
            
            print(f"Employee {name} is done with tasks ({all_tasks_count}/{len(completed_tasks)}):")
            
            for task in completed_tasks:
                print(f"\t {task.get('title')}")

