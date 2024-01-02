#!/usr/bin/python3
'''
Data in JSON format
'''
import json
import requests


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, verify=False)
    return response.json()


def get_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, verify=False)
    return response.json()


def organize_data(users, todos):
    user_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = {
            "username": user.get("username"),
            "tasks": []
        }

    for todo in todos:
        user_id = todo.get("userId")
        user_dict[user_id]["tasks"].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
        })

    return user_dict


def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    users = get_users()
    todos = get_todos()

    organized_data = organize_data(users, todos)

    export_to_json(organized_data, "todo_all_employees.json")
