from base import delete_todo_task

if __name__ == "__main__":
    while True:
        try:
            id = int(input("Enter the id of task you want to delete: "))
            break
        except:
            print("Please enter valid id value in (integer type)")
    endpoint = f"http://localhost:8000/api/todos/{id}/delete/"
    delete_todo_task(endpoint=endpoint)