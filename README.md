# Roberto's Portfolio API

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge)](LICENSE)
![Code Size](https://img.shields.io/github/languages/code-size/Pochetes/portfolio-api?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/Pochetes/portfolio-api?style=for-the-badge)
![Website Status](https://img.shields.io/website?down_color=red&down_message=offline&style=for-the-badge&up_color=green&up_message=up&url=http%3A%2F%2Flocalhost%3A8000)
![Open Issues](https://img.shields.io/github/issues-raw/Pochetes/portfolio-api?color=purple&style=for-the-badge)
![Closed Issues](https://img.shields.io/github/issues-closed-raw/Pochetes/portfolio-api?color=brown&style=for-the-badge)

The Roberto's Portfolio API is meant to retrieve data about my college life, career experiences and more. The goal of this API is to provide a data source for my GraphQL backend to display information for my portfolio website.

## Description

The api returns JSON responses in the `applications/json` format. It has a total of 6 endpoints that return specific data about me. More will be exaplined below.

### File Structure
```
.
├── LICENSE
├── README.md
├── __init__.py
├── __pycache__
│   ├── config.cpython-39.pyc
│   ├── database.cpython-39.pyc
│   ├── main.cpython-39.pyc
│   └── models.cpython-39.pyc
├── config.py
├── endpoints
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-39.pyc
│   ├── contacts
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── docs.md
│   │   ├── models.py
│   │   └── routers.py
│   ├── experiences
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── docs.md
│   │   ├── models.py
│   │   └── routers.py
│   ├── interests
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── docs.md
│   │   ├── models.py
│   │   └── routers.py
│   ├── projects
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── docs.md
│   │   ├── models.py
│   │   └── routers.py
│   ├── skills
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── models.cpython-39.pyc
│   │   │   └── routers.cpython-39.pyc
│   │   ├── docs.md
│   │   ├── models.py
│   │   └── routers.py
│   └── user
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-39.pyc
│       │   ├── models.cpython-39.pyc
│       │   └── routers.cpython-39.pyc
│       ├── docs.md
│       ├── models.py
│       └── routers.py
├── main.py
└── requirements.txt
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
- Authentication **(SOON!)**
- Deployed On Heroku **(SOON!)**
- Built under Docker environment OS **(SOON!)**
- Pylint & API Testing **(SOON!)**

## Endpoints

The base URL is currently: `http://localhost:8000/` --> (**SOON** `https://pochetes-dev.heroku-app.com`)

### User 👨🏼

You will be able to see my:

- name.
- email.
- brief description.

See a detailed description at: [User Docs](endpoints/user/docs.md)

### Contacts 📲
Here will be my **social media** links.

See a detailed description at: [Contacts Docs](endpoints/contacts/docs.md)

### Skills 🌟
This section holds the **technical** skills that I possess.

See a detailed description at: [Skills Docs](endpoints/skills/docs.md)

### Experiences 📈
Here will be the experiences that I've had throughout my journey pursuing **Software Engineering**.

See a detailed description at: [Experiences Docs](endpoints/experiences/docs.md)

### Interests 🤔
This will retrieve my interests **in** and **outside** the technology world.

See a detailed description at: [Interests Docs](endpoints/interests/docs.md)

### Projects 💡
This will return my software related projects that I have worked on.

See a detailed description at: [Projects Docs](endpoints/projects/docs.md)

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

## License

This repo is licensed under the MIT License.
