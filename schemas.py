from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

class Content(BaseModel):
    description: str

    class Config:
        from_attributes = True