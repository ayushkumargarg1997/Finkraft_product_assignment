from pydantic import BaseModel

class User_Login(BaseModel):
    email: str
    password: str 


class User_Signup(BaseModel):
    email: str
    password: str
    name: str
    phone: str

