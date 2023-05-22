import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]

    try:
        user_response = r.get(url + 'users/{}'.format(user_id), verify=False)
        user_response.raise_for_status()
        user_data = user_response.json()
        user_name = user_data['name']
    except (r.RequestException, ValueError, KeyError) as e:
        print(f"Error: Failed to retrieve user information. {str(e)}")
        sys.exit(1)

    try:
        todo_response = r.get(url + 'todos', params={'userId': user_id}, verify=False)
        todo_response.raise_for_status()
        todo_data = todo_response.json()
        completed_tasks = [task for task in todo_data if task['completed']]
    except (r.RequestException, ValueError, KeyError) as e:
        print(f"Error: Failed to retrieve TODO list. {str(e)}")
        sys.exit(1)

    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{len(todo_data)}):")
    for task in completed_tasks:
        print("\t" + task['title'])
