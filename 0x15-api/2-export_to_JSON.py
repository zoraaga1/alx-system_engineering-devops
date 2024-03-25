#!/usr/bin/python3
'''
Python script that export data in the JSON format.
'''
import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_data = requests.get(user_url, verify=False).json()

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)  # noqa
    todo_data = requests.get(todo_url, verify=False).json()

    username = user_data.get('username')

    tasks = [{"task": task.get("title"),
              "username": username,
              "completed": task.get("completed")} for task in todo_data]

    user_tasks = {}
    user_tasks[user_id] = tasks

    with open("{}.json".format(user_id), 'w') as json_file:
        json.dump(user_tasks, json_file)
