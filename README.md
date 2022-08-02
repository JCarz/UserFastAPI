# UserFastAPI
Simple Fast API framework use, with CRUD function
Fast API is a simple and modern high performance, webframework API that helps build APIs with Python

Fast API key Features:
- Fast and high performance comparison to Node JS and Go. 
-Fewer bugs, reduced by 40% of human errors
-Easy and robust get production ready code

Companies that use FAST API are Uber and Netflix

Install both fastAPI and uvicorn
pip install fastapi

pip install "uvicorn[standard]"


HTTP request methods:
HTTP defines a set of request methods that are used to indicate the desired action to the performed for a given resource. They are called HTTP verbs. Each is different in their own way but have common features are shared by a group of them.
GET,PUT,POST,DELETE


Start uvicorn main:app --reload

Asynchronous is intended to provide a simple way to provide a interface to async-capable Python webservers, frameworks, and apps. It is a asynchoronous callable. It takes a scope, with is dict containing details about the specific connection, send, a callable that lets the app send event messages to the client, and recieve a callable that lets the app recieve events from the client,Its constantly listing and ready send and recieve events from the app. 

SCOPE- Is the association of an entity such as a variable or a function that    returns vaild variables and can be used to reference the an entity.

DICT- Is a hash map, a hash map is different in other programming language. They're all the same thing: a key-value store or pair. 

Used libarys typing,uuid,enum, and pydantic 

Typing (Import)- is for the list AKA the database and the Optional keyword for some of the database's properties.

UUID (Import) - used for generating the unique identifier for the user model

Enum (Import) - is used for special data types that enable for a variable or a function to be a set of predefined values for the user model. 

Gender (Class) - is the Enum a user can either be male or female. This is a string datatype.

Roles (Class) - is the Enum a user can either be admin,user or student. This is a string datatype.

Pydantic is for setting the structure for the base model for the user. 

User Class - is the base model blueprint this contains the Optional UUID, f_name,l_name,m_name, gender class and roles class. 


Each user is hardcoded into main.py and is predefined. Every time the server is reloaded the created or modified users are erased. 


There are different sets of paths: 
"http://localhost:8000/",
"http://localhost:8000/docs",
"http://localhost:8000/api/v1/users"

Must be created in 
REST client and formated in JSON properties. No need for id it is generated. 

Put Method works best with the client but you need to get the server running grab a user ID from the DB. Create the request and user the body tab use the UserModel to help fill the body of the user you would like to change:
{
    "f_name": "str",
    "l_name": "str",
    "m_name": "str",
    "gender": "str",
    "roles": [
      "admin","user","student"
    ]
  }



