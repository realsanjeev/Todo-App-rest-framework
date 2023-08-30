from base import get_todo_lists

if __name__ == "__main__":
    endpoint = "http://localhost:8000/api/todo/"
    get_todo_lists(endpoint=endpoint)