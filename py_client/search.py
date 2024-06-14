from base import get_todo_lists

if __name__ == "__main__":
    endpoint = "http://localhost:8000/api/todos/search/"
    query = input("Enter query for todo list: ")

    get_todo_lists(endpoint=endpoint, params={"q": query})
