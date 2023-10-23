#!/usr/bin/python3
"""
Module Docs
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url_str.format(user_id))

    name = user.json().get('username')
    todos = requests.get(todos_url)

    todos_users = {}
    tasks = []

    for task in todos.json():
        if task.get('userId') == int(user_id):
            task_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user.json().get('username')
                    }
            tasks.append(task_dict)
        todos_users[user_id] = tasks

    file = user_id + '.json'

    with open(file, mode="w") as user_file:
        json.dump(todos_users, user_file)
