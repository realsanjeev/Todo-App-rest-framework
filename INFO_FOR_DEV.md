### Some Info
1. `from django.db.models.signals import post_save`:
   This import is used to access the `post_save` signal provided by Django's signals framework. Signals are a way for different parts of an application to communicate with each other and respond to specific events. The `post_save` signal is emitted by the Django ORM after an object's `save()` method is called and a new instance is created or an existing instance is updated. In the context of your code, you're using this signal to create a token for a user when a new user instance is created.

2. `from django.dispatch import receiver`:
   The `receiver` decorator is used to connect a function to a signal. In your case, you're using it to connect the `create_user_token` function to the `post_save` signal emitted by the `User` model. The `receiver` decorator allows you to specify which signal to listen for and which function to execute when the signal is emitted. This way, when a new user is created, the `create_user_token` function will be automatically triggered, and it will create a corresponding token for that user.

3. `from rest_framework.authtoken.models import Token`:
   This import is used to access the `Token` model provided by the Django Rest Framework's authentication token system. The authentication token system is used to manage authentication tokens for users. Tokens are often used in APIs to authenticate and authorize requests from clients. In your code, you're using the `Token` model to create new token instances for users. These tokens can then be used for authentication purposes when making API requests.


### DRF-Spectacular

DRF-Spectacular is a tool for generating OpenAPI 3.0 specifications for Django REST Framework (DRF) projects. It provides a flexible and powerful way to generate API documentation that is compatible with tools like Swagger UI, ReDoc, or other OpenAPI-driven interfaces. DRF-Spectacular is highly customizable, making it a popular choice for users looking to document their APIs.

**Key features of DRF-Spectacular include:**

1. **Automatic OpenAPI Spec Generation**: It automatically generates an OpenAPI schema from your DRF views, serializers, and models, saving you the hassle of manually writing OpenAPI specifications.

2. **Schema Customization**: You can customize the schema by using annotations, such as `@extend_schema`, `@extend_schema_view`, and others, to define detailed API information.

3. **Extensible**: DRF-Spectacular is designed to be extensible. You can adjust it to your needs by adding custom fields, filters, and descriptions, as well as overriding defaults for certain parts of the schema.

4. **Support for Nested Serializers**: DRF-Spectacular handles nested serializers and relationships in your models, making sure the API schema correctly reflects how models are related to each other.

5. **Error Handling**: DRF-Spectacular can automatically document error responses, which are crucial for a comprehensive API spec.

6. **Compatibility**: It supports compatibility with common tools like Swagger UI and ReDoc for easy integration into your project.
