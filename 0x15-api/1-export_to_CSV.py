#!/usr/bin/python3

'''
Export data in CSV format
'''

import csv
import requests
from sys import argv


def get_user_info(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, verify=False)
    return response.json()


def get_user_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url, verify=False)
    return response.json()


def export_to_csv(user_id, user_info, user_tasks):
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in user_tasks:
            taskwriter.writerow([int(user_id), user_info.get('username'),
                                 task.get('completed'), task.get('title')])


if __name__ == '__main__':
    if len(argv) > 1:
        user_id = argv[1]
        user_info = get_user_info(user_id)
        user_tasks = get_user_tasks(user_id)
        export_to_csv(user_id, user_info, user_tasks)
