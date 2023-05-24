import requests
import sys

if __name__ == "__main__":
    user_id = str(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users'
    endpoints = ["posts", "comments", "albums", "photos", "todos", "users"]

    r = requests.get(url).json()
    name = None
    for i in r:
        if i.get('id') == int(user_id):
            name = i['name']
            break

    td = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    ttl_tasks = 0
    comp_tasks = []
    for i in td:
        if i.get("userId") == int(user_id):
            ttl_tasks += 1
            if i.get("completed"):
                comp_tasks.append(i.get('title'))

    print("Employee {} is done with tasks ({}/{}):"
          .format(name, len(comp_tasks), ttl_tasks))

    for task in comp_tasks:
        print("\t{}".format(task))
