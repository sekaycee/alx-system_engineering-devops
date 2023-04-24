#!/usr/bin/python3
''' Export to-do list info of a given employee ID to CSV format '''
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    userid = sys.argv[1]
    user = requests.get(url + 'users/' + userid).json()
    name = user.get('username')
    todos = requests.get(url + 'todos?userId=' + userid).json()
    c_tasks = [[userid, name, todo.get('completed'), todo.get('title')]
               for todo in todos]

    with open('{}.csv'.format(userid), mode='w') as employee_file:
        for task in c_tasks:
            csv.writer(employee_file, quoting=csv.QUOTE_ALL).writerow(task)
