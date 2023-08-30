import requests

base_url = "http://localhost:8000"

# Authenticate and obtain a token
auth_url = f"{base_url}/api-auth/login"
response = requests.post(auth_url, data={"username": "admin", "password": "admin"})
# print(f"{'*'*30}\nresponse: {response.content}\n{'*'*30}")
with open("response.htm", "wb") as fp_h:
    fp_h.write(response.content)
token = response.json().get("token")

print(f"token: {token}")
if token:
    # include the token in header
    header = {"Authorization": f"Token {token}"}

    # make get request
    tasks_url = f"{base_url}/api/"
    tasks_response = requests.get(tasks_url, headers=header)

    print(tasks_response.json())
else:
    print("Authentication failed")