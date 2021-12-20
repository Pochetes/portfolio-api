from pydantic import BaseSettings

# CHANGE  
class DatabaseSettings(BaseSettings):
    DB_NAME: str = "portfolio"
    DB_URI: str = "MONGODB_URI"

    class Config:
        orm_mode = True

# CHANGE
class MiddlewareSettings(BaseSettings):
    CORS_CRED: bool = True
    CORS_METHODS: list = ["*"]
    CORS_HEADERS: list = ["*"]
    CORS_ORIGINS: list = [
        "http://pochetes.herokuapp.com/personal",
        "http://pochetes.herokuapp.com/experiences",
        "http://pochetes.herokuapp.com/projects",
        "https://pochetes.herokuapp.com/personal",
        "https://pochetes.herokuapp.com/experiences",
        "https://pochetes.herokuapp.com/projects",
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:8000/personal",
        "http://localhost:8000/experiences",
        "http://localhost:8000/projects",
    ]

    class Config:
        orm_mode = True    

# CHANGE
class MetadataSettings(BaseSettings):
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

    class Config:
        orm_mode = True

# container class for all settings        
class Settings(BaseSettings):
    db: DatabaseSettings
    md: MiddlewareSettings
    mt: MetadataSettings

    class Config:
        orm_mode: True

settings = Settings(db=DatabaseSettings(), 
                    md=MiddlewareSettings(), 
                    mt=MetadataSettings())
