from base import delete_todo_task


def get_task_id():
    while True:
        try:
            id = int(input("Enter the ID of the task you want to delete: "))
            return id
        except ValueError:
            print("Please enter a valid integer value for the ID.")


if __name__ == "__main__":
    task_id = get_task_id()
    endpoint = f"http://localhost:8000/api/todos/{task_id}/delete/"
    response = delete_todo_task(endpoint=endpoint)
