#!/usr/bin/python3
"""
Script that fetches information about a given employee's ID using an API.
"""

import csv
import json
import requests
import sys
import warnings

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    # Retrieve user ID from command-line argument
    user_id = sys.argv[1]

    # Retrieve user data
    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url, verify=False)
    user_data = json.loads(response.text)
    username = user_data[0].get('username')

    # Retrieve tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url, verify=False)
    tasks = json.loads(response.text)

   # Create and write to CSV file
    file_name = f'{user_id}.csv'
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            completed_status = "False"
            if task.get('completed'):
                completed_status = "True"
            writer.writerow([user_id, username, completed_status, task.get('title')])

    # Print success message
    print(f"Data exported to {user_id}.csv")
