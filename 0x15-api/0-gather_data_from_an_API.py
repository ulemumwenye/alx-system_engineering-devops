#!/usr/bin/python3
"""script that fetches info about a given employee using an api
 
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
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
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
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
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
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for i in range(total_tasks):
        if requests.get(f"https://jsonplaceholder.typicode.com/todos/{i + 1}").json().get("completed"):
            print("\t{}".format(requests.get(f"https://jsonplaceholder.typicode.com/todos/{i + 1}").json().get("title")))
