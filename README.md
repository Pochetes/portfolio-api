# Roberto's Portfolio API

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE)
![Code Size](https://img.shields.io/github/languages/code-size/Pochetes/portfolio-api?style=flat-square)
![Website](https://img.shields.io/website?down_color=red&down_message=offline&style=flat-square&up_color=green&up_message=online&url=https%3A%2F%2Frobertos-api.herokuapp.com%2Fdocs)
![Open Issues](https://img.shields.io/github/issues-raw/Pochetes/portfolio-api?color=purple&style=flat-square)
![Closed Issues](https://img.shields.io/github/issues-closed-raw/Pochetes/portfolio-api?color=brown&style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/pochetes/portfolio-api?style=flat-square)

The Roberto's Portfolio API is meant to retrieve data about my college life, career experiences and more. The goal of this API is to provide a data source for my GraphQL backend to display information for my portfolio website.

## Description

The api returns JSON responses in the `applications/json` format. It has a total of 6 endpoints that return specific data about me. More will be explained below.

### File Structure
```
.
├── Dockerfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── __pycache__
│   ├── config.cpython-39.pyc
│   ├── database.cpython-39.pyc
│   ├── main.cpython-39.pyc
│   ├── models.cpython-39.pyc
│   └── setup.cpython-39.pyc
├── api-tests.json
├── config.py
├── docker-compose.yml
├── endpoints
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── auth.cpython-39.pyc
│   │   └── utils.cpython-39.pyc
│   ├── auth.py
│   ├── contacts
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── models.py
│   │   └── routers.py
│   ├── experiences
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── models.py
│   │   └── routers.py
│   ├── interests
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── models.py
│   │   └── routers.py
│   ├── projects
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── models.py
│   │   └── routers.py
│   ├── skills
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── models.py
│   │   └── routers.py
│   ├── user
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── models.py
│   │   └── routers.py
│   └── utils.py
├── main.py
├── media
│   └── gifs
│       ├── GETmethod.gif
│       ├── POSTmethod.gif
│       └── Params.gif
├── requirements.txt
└── script.sh

17 directories, 68 files
```

### Technologies Used

The API is implemented in:
- the **Python** language, using a framework known as **FastAPI**, which automatically renders a **Swagger** Documentation Spec.
- **MongoDB**, the NoSQL database, in order to store all my data. Currently under the Python driver, **Pymongo**.
- **Uvicorn**, a server implementation, that enables an ecosystem of Python web frameworks such as the one I'm currently using.
- **Pydantic**, a data validation and settings management tool that helps define my models and schema more efficiently.

## Features

This API provides many features that make it lighting-fast:
- CORS Middleware
- lru_cache Decorator
- Easy-To-Use Documentation
- Modularized Application
- MongoDB CRUD Operations
- Error & Exception Handling
- Pylint & API Testing
- Auth0 Authentication & Security
- Built under Docker environment OS
- Deployed On Heroku

## Endpoints

The base URL is currently: `https://robertos-api.herokuapp.com`

### User 👨🏼

You will be able to see my:

- name.
- email.
- brief description.

See a detailed description at: [User Docs](endpoints/user/README.md)

### Contacts 📲
Here will be my **social media** links.

See a detailed description at: [Contacts Docs](endpoints/contacts/README.md)

### Skills 🌟
This section holds the **technical** skills that I possess.

See a detailed description at: [Skills Docs](endpoints/skills/README.md)

### Experiences 📈
Here will be the experiences that I've had throughout my journey pursuing **Software Engineering**.

See a detailed description at: [Experiences Docs](endpoints/experiences/README.md)

### Interests 🤔
This will retrieve my interests **in** and **outside** the technology world.

See a detailed description at: [Interests Docs](endpoints/interests/README.md)

### Projects 💡
This will return my software related projects that I have worked on.

See a detailed description at: [Projects Docs](endpoints/projects/README.md)

## Documentation

Thanks to FastAPI, a documentation page is automatically rendered for us. This follows the OpenAPI Spec rules.

To see the docs, go to [docs](https://robertos-api.herokuapp.com) when it's deployed.

***Update**: The `/docs` endpoint will automatically be accessed when using the base url.

### Using a `GET` method

The `GET` method allows you to access all the data from a specific resource. It is done, like so:

![GET method](media/GETmethod.gif)

### Using a `POST` method

The `POST` method allows you to create a new data entry for a specific resource. There will be a Request body in which you will fill out all contents needed, like so:

![POST method](media/POSTmethod.gif)

### Using a method that has a path parameter

A method that has a path parameter usually requires some sort of input to find, update, delete a specific resource. In this example, we are finding a single project by an `id` path parameter. To do this, copy the parameter from the first `GET` method and use it as the current path parameter, like so:

![Params](media/Params.gif)

## Authentication

The `POST`, `PUT`, and `DELETE` endpoints are protected using 0Auth authentication. I am the only person that's able to make those changes (unless you were able to get my access token, that is) and authenticate the endpoints. It is secured through a JWT-formatted access token. After some time, a new token is generated, making it difficult for hackers to access these data points. The hashing algorithm used is **RS256**, or RSA Signature with SHA-256.

## Configuration

To run this project, you need a couple things:

- MongoDB connection
- Virtual environment
- Installed Dependencies

### Get Project

You can clone this project using the following command:

Using HTTPS (I believe it's deprecated)
```
git clone https://github.com/Pochetes/portfolio-api.git
```

Using SSH
```
git clone git@github.com:Pochetes/portfolio-api.git
```

### Database Connection

To get a MongoDB database, sign in (or create an account if you haven't already) to MongoDB Atlas. Then, create a new cluster and find the connection string in which you will put in a `.env` file, like so:

```python
# Unix:
export MONGODB_URI = "mongodb+srv://Username:Password@mongodb-cluster-name.foihs.mongodb.net/db-name?retryWrites=true&w=majority"
```

For more details, visit [connect to a MongoDB database](https://docs.atlas.mongodb.com/).

### Creating a virtual environment

To create a virtual environment, create a hidden `virtualenv` file, like so:
```
python3 -m venv name-of-env
```
Then, activate it, like so:
```
source name-of-env/bin/activate
```

### Installing Dependencies

To install, run the command:
```
python3 -m pip install -r requirements.txt
```

### Running the Server

To run the server, run:
```
python main.py
```

### Creating a Docker Container

First, build the docker image as provided in the `Dockerfile` using this command:
```
docker build -t portfolio-api-image .
```
Afterwards, make a new container using the `docker run` command:
```
docker run -d \
--name portfolio-api-container \
-p 8080:8080 \
<docker_image_id>
```
Now you will be able to access the containerized application on your local machine!

## License

This repo is licensed under the MIT License.
