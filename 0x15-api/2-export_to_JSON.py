#!/usr/bin/python3
''' Export to-do list information for a given employee ID to JSON format '''
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(userid)).json()
    name = user.get('username')
    todos = requests.get(url + 'todos?userId={}'.format(userid)).json()
    c_tasks = [{'task': todo.get('title'), 'completed': todo.get('completed'),
                'username': name} for todo in todos]

    with open(userid + '.json', mode='w') as emp_file:
        json.dump({userid: c_tasks}, emp_file)
