#!/usr/bin/python3

import requests
import json

def export_employee_todo_data(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0]['username']
        employee_data = []

        for todo in todos:
            task_title = todo['title']
            task_completed = todo['completed']
            employee_data.append({"task": task_title, "completed": task_completed, "username": employee_name})

        # Create the JSON file name based on the employee ID
        file_name = f"{employee_id}.json"

        # Write the employee's TODO data to the JSON file
        with open(file_name, 'w') as json_file:
            json.dump({employee_id: employee_data}, json_file)

        print(f"Exported TODO data for Employee ID {employee_id} to {file_name}")
    else:
        print(f"Failed to retrieve TODO list for Employee ID {employee_id}. Error: {response.status_code}")

# Example usage: passing employee ID 1
export_employee_todo_data(1)
