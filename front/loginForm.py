import requests

data = {
    "usuario": "admin",
    "contrasena": "I9f04&~RakBS",
    "rol": "CANDIDATE"
}

r = requests.post('http://localhost:5000/login-candidate', json=data)
token = r.json()['token']

# save the token in a file for later use
with open('token.txt', 'w') as f:
    f.write(token)
