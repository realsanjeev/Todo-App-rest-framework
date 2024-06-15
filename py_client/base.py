import os

import requests
from auth import SECRECT_FILE, authenticate

# Check for the existence of the secret file
if os.path.exists(SECRECT_FILE):
    with open(SECRECT_FILE, "r") as fp:
        token = fp.read().strip()
else:
    # Authenticate and obtain the token
    token = authenticate()

# Prepare the authorization header
header = {"Authorization": f"Bearer {token}"}


def get_todo_lists(
    endpoint: str,
    json_payload: dict = None,
    data: dict = None,
    params: dict = None,
    headers: dict = header,
):
    print("*" * 4, f" {endpoint} ", "*" * 4)
    response = requests.get(endpoint, params=params, data=data, headers=headers)
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


def post_todo_task(
    endpoint: str,
    json_payload: dict = None,
    data: dict = None,
    params: dict = None,
    headers: dict = header,
):
    print("*" * 4, f" {endpoint} ", "*" * 4)
    response = requests.post(
        endpoint, json=json_payload, data=data, params=params, headers=headers
    )
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


def update_todo_task(
    endpoint: str,
    json_payload: dict = None,
    headers: dict = header,
):
    print("*" * 4, f" {endpoint} ", "*" * 4)
    response = requests.put(endpoint, json=json_payload, headers=headers)
    try:
        # json_response = response.json()

        # print(response.status_code)
        # print("Updated data: ", json_response)
        with open("update.html", "wb") as fp:
            fp.write(response.content)
        print(response.content)
    except requests.ConnectionError:
        raise Exception("Connection Error")
    except requests.JSONDecodeError:
        raise Exception("JSON error")
    except requests.RequestException as err:
        raise Exception(f"Request Error Exception: {err}")
    # return json_response


def delete_todo_task(
    endpoint: str,
    headers: dict = header,
):
    print("*" * 4, f" {endpoint} ", "*" * 4)
    response = requests.delete(endpoint, headers=headers)

    try:
        if response.status_code == 200:
            json_response = response.json()
            print("Deleted data: ", json_response)
        else:
            print(response.json())
        return response
        # print(response.content)
    except requests.ConnectionError:
        raise Exception("Connection Error")
    except requests.JSONDecodeError:
        raise Exception("JSON error")
    except requests.RequestException as err:
        raise Exception(f"Request Error Exception: {err}")


if __name__ == "__main__":
    endpoint = "http://localhost:8000/api/todos/"
    get_todo_lists(endpoint=endpoint)
