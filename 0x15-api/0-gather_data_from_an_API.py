#!/usr/bin/python3
''' Return to-do list information for a given employee ID '''
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos?userId={}'.format(sys.argv[1])).json()
    c_tasks = [todo for todo in todos if todo.get('completed') is True]

    print('Employee {} is done with tasks'.format(user.get('name')), end='')
    print('({}/{}):'.format(len(c_tasks), len(todos)))
    for task in c_tasks:
        print('\t {}'.format(task.get('title')))
