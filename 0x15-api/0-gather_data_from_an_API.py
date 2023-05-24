#!/usr/bin/python3
"""
Script that fetches information about a given employee's ID using an API.
"""

import json
import requests
import sys


BASE_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":
    """
    Retrieves information about a given employee's ID and displays their completed tasks.
    """
    user_id = sys.argv[1]

    # Get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = f"{BASE_URL}/users?id={user_id}"

    # Get info from API with SSL certificate verification
    response = requests.get(user_url, verify=True)
    data = response.json()

    # Extract user data, in this case, the name of the employee
    name = data[0].get('name')

    # Get user info about todo tasks e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = f"{BASE_URL}/todos?userId={user_id}"

    # Get info from API with SSL certificate verification
    response = requests.get(tasks_url, verify=True)
    tasks = response.json()

    # Initialize completed count as 0 and find the total number of tasks
    completed = 0
    total_tasks = len(tasks)

    # Initialize an empty list for completed tasks
    completed_tasks = []

    # Loop through tasks counting the number of completed tasks
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    # Print the output in the required format
    print(f"Employee {name} is done with tasks ({completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")
