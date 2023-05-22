#!/usr/bin/python3

import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if response.status_code == 200:
        todos = response.json()
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        employee_name = todos[0]['username']

        # Print the employee's TODO list progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        print(f"{employee_name}: name of the employee")
        print(f"{num_completed_tasks}: number of completed tasks")
        print(f"{total_tasks}: total number of tasks, which is the sum of completed and non-completed tasks")

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Failed to retrieve TODO list for employee ID {employee_id}. Error: {response.status_code}")

# Example usage: passing employee ID 1
get_employee_todo_progress(1)
