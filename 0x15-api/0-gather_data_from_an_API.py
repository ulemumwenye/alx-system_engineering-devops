#!/usr/bin/env python3
"""
This script retrieves user information and task data from an API,
and displays the completed tasks for a given user.

Usage: python script_name.py user_id

Arguments:
    user_id: ID of the user to fetch completed tasks for.

Example: python script_name.py 1
"""

import requests
import sys


if __name__ == "__main__":
    # Retrieve user ID from command-line argument
    user_id = str(sys.argv[1])

    # Base URL for retrieving user information
    url = 'https://jsonplaceholder.typicode.com/users'

    # List of different endpoints that can be accessed
    endpoints = ["posts", "comments", "albums", "photos", "todos", "users"]

    # Retrieve user data from API
    r = requests.get(url).json()

    # Find the name of the user with the given ID
    name = None
    for i in r:
        if i.get('id') == int(user_id):
            name = i['name']
            break

    # Retrieve task data from API
    td = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    # Initialize variables for total and completed tasks
    ttl_tasks = 0
    comp_tasks = []

    # Count the total and completed tasks for the user
    for i in td:
        if i.get("userId") == int(user_id):
            ttl_tasks += 1
            if i.get("completed"):
                comp_tasks.append(i.get('title'))

    # Print the output in the required format
    print("Employee {} is done with tasks ({}/{}):"
          .format(name, len(comp_tasks), ttl_tasks))

    # Print the titles of the completed tasks
    for task in comp_tasks:
        print("\t{}".format(task))
