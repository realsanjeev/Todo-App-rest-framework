from base import get_todo_lists

if __name__ == "__main__":
    endpoint = "http://localhost:8000/api/todos/"
    get_todo_lists(endpoint=endpoint)