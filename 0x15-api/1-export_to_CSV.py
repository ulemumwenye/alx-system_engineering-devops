import csv
import json
import requests
import sys
import urllib3

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    user_id = sys.argv[1]

    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url, verify=False)
    user_data = json.loads(response.text)
    username = user_data[0].get('username')

    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url, verify=False)
    tasks = json.loads(response.text)

    file_name = '{}.csv'.format(user_id)
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            completed_status = "Yes" if task.get('completed') else "No"
            writer.writerow([user_id, username, completed_status, task.get('title')])

    print("Data exported to {}.csv".format(user_id))
