#!/usr/bin/python3
''' Export to-do list information for a given employee ID to JSON format '''
import json
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]
    user = requests.get(url + 'users/' + userid).json()
    todos = requests.get(url + 'todos?userId=' + userid).json()
    c_tasks = [{'task': todo.get('title'), 'completed': todo.get('completed'),
                'username': user.get('username')} for todo in todos]

    with open(userid + '.json', mode='w') as emp_file:
        json.dump({userid: c_tasks}, emp_file)
