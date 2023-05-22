#!/usr/bin/python3

import requests
import csv

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
            employee_data.append([employee_id, employee_name, task_completed, task_title])

        # Create the CSV file name based on the employee ID
        file_name = f"{employee_id}.csv"

        # Write the employee's TODO data to the CSV file
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(employee_data)

        print(f"Exported TODO data for Employee ID {employee_id} to {file_name}")
    else:
        print(f"Failed to retrieve TODO list for Employee ID {employee_id}. Error: {response.status_code}")

# Example usage: passing employee ID 1
export_employee_todo_data(1)
