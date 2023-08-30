import os
import json
import requests
from auth import authenticate, SECRECT_FILE

# Check for the existence of the secret file
if os.path.exists(SECRECT_FILE):
    with open(SECRECT_FILE, "r") as fp:
        token = fp.read()
else:
    # Authenticate and obtain the token
    token = authenticate()

# Prepare the authorization header
header = {"Authorization": f"Bearer {token}"}

def get_todo_lists(endpoint: str,
                   json_payload: dict = None,
                   data: dict = None,
                   params: dict = None,
                   headers: dict = header):
    print("*" * 4, f" {endpoint} ", "*" * 4)
    response = requests.get(endpoint,
                            json=json_payload,
                            data=data,
                            params=params,
                            headers=headers)
    try:
        json_response = response.json()
        print(json_response)
        # print(response.content)
    except requests.ConnectionError:
        raise Exception("Connection Error")
    except requests.JSONDecodeError:
        raise Exception("JSON error")
    except requests.RequestException as err:
        raise Exception(f"Request Error Exception: {err}")
    return json_response

if __name__ == "__main__":
    endpoint = "http://localhost:8000/api/todo/"
    get_todo_lists(endpoint=endpoint)
