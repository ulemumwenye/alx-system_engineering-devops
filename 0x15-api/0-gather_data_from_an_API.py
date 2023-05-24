#!/usr/bin/python3
"""
Script that fetches info about a given employee using an API.
"""

import json
import requests
import sys


def get_employee_name(employee_id):
    """
    Retrieves the name of the employee with the given ID from the API.

    Args:
        employee_id: ID of the employee.

    Returns:
        Name of the employee.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url, verify=False)
    data = response.json()
    return data.get("name")


def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list progress for the employee with the given ID from the API.

    Args:
        employee_id: ID of the employee.

    Returns:
        A tuple containing the number of completed tasks and the total number of tasks.
    """
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url, verify=False)
    data = response.json()

    total_tasks = len(data)
    completed_tasks = sum(task.get("completed") for task in data)

    return completed_tasks, total_tasks


if __name__ == "__main__":
    # Retrieve employee ID from command-line argument
    employee_id = sys.argv[1]

    # Get the name of the employee
    employee_name = get_employee_name(employee_id)

    # Get the TODO list progress for the employee
    completed_tasks, total_tasks = get_employee_todo_progress(employee_id)

    # Print the output in the required format
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for i in range(total_tasks):
        url = "https://jsonplaceholder.typicode.com/todos/{}".format(i + 1)
        response = requests.get(url, verify=False)
        task = response.json()
        if task.get("completed"):
            print("\t{}".format(task.get("title")))
