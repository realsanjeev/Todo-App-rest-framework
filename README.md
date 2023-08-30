# Todo Task API Framework

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

### Some Info
1. `from django.db.models.signals import post_save`:
   This import is used to access the `post_save` signal provided by Django's signals framework. Signals are a way for different parts of an application to communicate with each other and respond to specific events. The `post_save` signal is emitted by the Django ORM after an object's `save()` method is called and a new instance is created or an existing instance is updated. In the context of your code, you're using this signal to create a token for a user when a new user instance is created.

2. `from django.dispatch import receiver`:
   The `receiver` decorator is used to connect a function to a signal. In your case, you're using it to connect the `create_user_token` function to the `post_save` signal emitted by the `User` model. The `receiver` decorator allows you to specify which signal to listen for and which function to execute when the signal is emitted. This way, when a new user is created, the `create_user_token` function will be automatically triggered, and it will create a corresponding token for that user.

3. `from rest_framework.authtoken.models import Token`:
   This import is used to access the `Token` model provided by the Django Rest Framework's authentication token system. The authentication token system is used to manage authentication tokens for users. Tokens are often used in APIs to authenticate and authorize requests from clients. In your code, you're using the `Token` model to create new token instances for users. These tokens can then be used for authentication purposes when making API requests.

