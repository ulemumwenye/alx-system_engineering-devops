#!/usr/bin/python3
"""script that fetches info api"""
import json
import requests
import sys


BASE_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    """
    Retrieves info about an employee's ID.
    """
    user_id = sys.argv[1]

    # Get user info, e.g., https://jsonplaceholder.typicode.com/users/1/
    user_url = f"{BASE_URL}/users?id={user_id}"

    # Get info from API
    response = requests.get(user_url, verify=True)
    data = response.json()

    # Extract user data, in this case,
    name = data[0].get('name')

    # Get user info about todo tasks, e.g.,
    tasks_url = f"{BASE_URL}/todos?userId={user_id}"

    # Get info from API
    response = requests.get(tasks_url, verify=True)
    tasks = response.json()

    # Initialize completed count as
    completed = 0
    total_tasks = len(tasks)

    # Initialize an empty list for completed tasks
    completed_tasks = []

    # Loop through tasks counting
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    # Print the output in the required format
    output_format = "Employee {} is done with tasks ({}/{}):"
    print(output_format.format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
