#!/usr/bin/python3
"""
Module Doc
"""
import sys
import requests
import csv


if __name__ == "__main__":
    user_id = sys.argv[1]
    url_str = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(url_str, user_id)
    todos_str = '{}todos?userId={}'.format(url_str, user_id)
    file = '{}.csv'.format(user_id)

    res = requests.get(user_str)
    username = res.json().get('username')

    res = requests.get(todos_str)
    tasks = []
    for task in res.json():
        tasks.append([user_id,
                       name,
                       task.get('completed'),
                       task.get('title')])

    with open(file, mode='w') as emp_file:
        emp_writer = csv.writer(emp_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in l_task:
            emp_writer.writerow(task)
