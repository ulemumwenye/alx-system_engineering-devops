#!/usr/bin/python3
"""Script that fetches info about a given employee's ID using an API and exports the data in CSV format."""
import csv
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Get user info
    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url)
    data = response.json()
    name = data[0].get('name')

    # Get user tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url)
    tasks = response.json()

    # Export data to CSV file
    file_name = '{}.csv'.format(user_id)
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            completed_status = "Completed" if task.get('completed') else "Incomplete"
            task_title = task.get('title')
            writer.writerow([user_id, name, completed_status, task_title])

    print("Data exported to file: {}".format(file_name))
