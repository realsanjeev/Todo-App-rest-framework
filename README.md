# Todo Task API Framework

## Setup Instructions

### Step 1: Clone the GitHub Repository

Clone the repository to your local machine using the following command:
```bash
git clone <repository-url>
```

### Step 2: Initialize the Virtual Environment and Install Dependencies

Navigate to the project directory and create a virtual environment:
```bash
cd Todo-App-rest-framework
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Migrate the Database and Run the Django Application

Navigate to the `todo_task` directory, apply migrations, and start the Django development server:
```bash
cd todo_task
python manage.py migrate
python manage.py runserver
```

The **Todo Task API Framework** is designed to provide API responses that can be seamlessly integrated with front-end web applications, such as React.js projects or other web applications, allowing them to request API data and present information to users effectively.

This project leverages the powerful features of the `rest_framework` library to facilitate various core concepts:

## 1. Authentication
To ensure secure interactions that involve modifying the database, user authentication is required. This framework employs the robust token-based authentication system provided by `rest_framework`.

## 2. CRUD Operations
Authenticated users have the ability to perform Create, Read, Update, and Delete (CRUD) operations. The system's permissions and authentication processes can be tailored to specific requirements by utilizing custom classes.

## 3. Pagination
The framework includes a built-in pagination service. This practice is essential when retrieving data from the backend and implementing it on the frontend, as it optimizes data transfer and enhances user experience.

## 4. Search Functionality
Search functionality is a fundamental feature of the framework. Users can easily search for specific records using queries, making data retrieval efficient and user-friendly.

## 5. API Endpoint Links
Each operation within the framework is associated with a dedicated API endpoint. This endpoint provides direct access to the respective record, facilitating smooth interaction between the front-end application and the backend API.

By integrating these core concepts, the **Todo Task API Framework** offers a comprehensive solution for building interactive and feature-rich web applications while adhering to industry best practices and ensuring data security.

## Todo App

The Todo App is a task management application that allows users to create, delete, and mark tasks as completed. While the rendering service provides basic functionality, additional features are available through the REST API.

### Features Available:

1. **Add Task**
   - Users can create new tasks by providing a title and optional description.

2. **Delete Task**
   - Users can remove tasks from the list.

3. **Mark Task as Completed**
   - Users can mark tasks as completed to track their progress.

### Additional Features (Available in REST API):

1. **Authentication**
   - Provides secure access control for users, ensuring that only authorized individuals can interact with the application.

2. **Pagination**
   - Manages large lists of tasks by splitting them into manageable pages, improving the user experience.

3. **Searching**
   - Enables users to search for specific tasks based on keywords or criteria, making it easier to find and manage tasks.

> If you only want rest_api service remove `todo_apps` from settings and delete `todo_apps` dir.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## Contact Me

<table>
  <tr>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/instagram.png" alt="Instagram" width="50" height="50"></td>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/twitter.png" alt="Twitter" width="50" height="50"></td>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/github.png" alt="GitHub" width="50" height="50"></td>
    <td><img src="https://github.com/realsanjeev/protfolio/blob/main/src/assets/images/linkedin-logo.png" alt="LinkedIn" width="50" height="50"></td>
  </tr>
</table>
