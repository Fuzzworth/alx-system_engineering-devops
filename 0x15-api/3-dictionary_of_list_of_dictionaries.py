#!/usr/bin/python3
"""
Module Docs
"""
import json
import requests
import sys


if __name__ == "__main__":
    users_j = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos_j = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    todos = {}

    for user in users_j:
        tasks = []
        for task in todos_j:
            if task.get('userId') == user.get('id'):
                task_dict = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')
                        }
                tasks.append(task_dict)
        todos[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(todos, file)
