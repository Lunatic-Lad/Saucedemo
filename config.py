import os
import json


BASE_PATH = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(BASE_PATH, "files", "creds.json")
print(BASE_PATH)
print(path)
with open(path, 'r') as file:
    creds_data = json.load(file)
print(creds_data)


USERNAME = creds_data['username']
PASSWORD = creds_data['password']
print(USERNAME)
print(PASSWORD)
