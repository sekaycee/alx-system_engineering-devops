#!/usr/bin/python3
''' Export to-do list information of all employees to JSON format '''
import json
import requests
import sys

if __name__ == '__main__':
    tasks_dump = {}
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    for user in users:
        name = user.get('username')
        userid = user.get('id')
        todos = requests.get(url + 'todos?userId={}'.format(userid)).json()
        c_tasks = [{'username': name, 'task': todo.get('title'),
                    'completed': todo.get('completed')} for todo in todos]
        tasks_dump[userid] = c_tasks

    with open('todo_all_employees.json', mode='w') as emp_file:
        json.dump(tasks_dump, emp_file)
