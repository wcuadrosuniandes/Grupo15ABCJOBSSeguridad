import requests

# read token form file
with open('token.txt', 'r') as f:
    token = f.read()

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}

data = {
    "data": "data insert"
}

r = requests.post('http://127.0.0.1:5000/register-candidate', json=data, headers=headers)

print(r.json())
