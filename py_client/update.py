from base import update_todo_task

if __name__ == "__main__":
    while True:
        try:
            id = int(input("Enter the id of task you want to update: "))
            break
        except ValueError:
            print("Please enter valid id value in (integer type)")
    new_data = {"task": "Task updated"}
    endpoint = f"http://localhost:8000/api/todos/{id}/update"
    update_todo_task(endpoint=endpoint, json_payload=new_data)
