#!/usr/bin/python3
'''
A script to export data in the JSON format for all employees.
'''

import json
import requests

if __name__ == '__main__':
    url_users = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(url_users, verify=False).json()

    all_tasks = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"  # noqa
        todos_data = requests.get(url_todos, verify=False).json()
        tasks = [{"username": username,
                  "task": task.get("title"),
                  "completed": task.get("completed")} for task in todos_data]
        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_tasks, json_file)
