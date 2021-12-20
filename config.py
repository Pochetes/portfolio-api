from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Roberto's Portfolio API"
    DEBUG_MODE: bool = True
    VERSION: str = "1.0.0"
    CONTACT: dict = {
        "name": "Roberto Martinez",
        "email": "robertomiguel2001@gmail.com"
    }
    LICENSE: dict = {
        "name": "MIT",
        "url": "https://choosealicense.com/licenses/mit"
    }
    DB_NAME: str = "portfolio"
    DB_URL: str = "MONGODB_URI"
    DESC: str = """
This is an API that retrieves information about Roberto Martinez's personal and work life. 🚀

For now, we have 5 broad endpoints that describe everything there is to know. However, some of the
endpoint methods will be unavailable to users as they are authenticated for my use only.

### User 👨🏼

You will be able to see my:
-name.
-email.
-brief description.

### Contacts 📲

Here will be my **social media** links.

### Skills 🌟

This section holds the **technical** skills that I possess.

### Experiences 📈

Here will be the experiences that I've had throughout my journey pursuing **Software Engineering**.

### Interests 🤔

This will retrieve my interests **in** and **outside** the technology world.

### Projects 💡

This will return my software related projects that I have worked on.
"""

settings = Settings()
